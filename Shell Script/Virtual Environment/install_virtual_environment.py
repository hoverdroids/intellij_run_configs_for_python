import platform
import tkinter
from sys import exception
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

import os
import sys
import venv

DIALOG_TITLE = "Create Virtual Environment"

def open_directory_if_desired(dialog_title: str, directory: str):
    if not os.path.isdir(directory):
        messagebox.showerror(
            title=dialog_title,
            message="The directory does not exist",
            detail=directory
        )
        return

    do_open_directory:bool = messagebox.askyesno(
        title=dialog_title,
        message="Open directory?",
        detail=directory
    )
    if not do_open_directory:
        return

    os_name = platform.system().lower()
    if do_open_directory and os_name == "windows":
        os.startfile(directory)
    elif do_open_directory and os_name == "darwin":#macOs
        os.system(f"open {directory}")
    elif do_open_directory and os_name == "linux":
        os.system(f"xdg-open {directory}")
    else:
        messagebox.showerror(
            title=dialog_title,
            message=f"Couldn't open directory. Only Windows, MacOS, and Linux are supported",
            detail=directory
        )

def is_safe_to_create_directory(dialog_title: str, directory: str) -> bool|None:
    if os.path.exists(directory):
        do_override_existing_directory: bool|None = messagebox.askyesnocancel(
            title=dialog_title,
            message=f"The directory already exists; override it?",
            detail=directory
        )

        if do_override_existing_directory is None:
            print(f"User cancelled the operation")
            return None
        elif not do_override_existing_directory:
            print(f"User opted not to override the existing directory")
            return False

    return True

def ask_user_for_virtual_environment_directory_name(dialog_title: str) -> str | None:
    root = tkinter.Tk()
    root.withdraw() # Hide the main window

    directory_name = ".venv"
    user_entered_directory_name = simpledialog.askstring(
        title=dialog_title,
        prompt="Enter the name of the virtual environment directory",
        initialvalue=directory_name
    )
    root.destroy()

    if user_entered_directory_name is None:
        print(f"User cancelled the operation")
        return None
    else:
        print(f"User set the virtual environment directory name to {user_entered_directory_name}")
        return user_entered_directory_name

def ask_user_to_select_virtual_environment_directory(dialog_title: str, initial_directory: str) -> str | None:
    root = tkinter.Tk()
    root.withdraw() # Hide the main window

    user_selected_directory = filedialog.askdirectory(
        title=dialog_title,
        initialdir=initial_directory
    )

    root.destroy()

    if user_selected_directory == "":
        print(f"User cancelled the operation")
        return None
    else:
        print(f"User selected directory {user_selected_directory}")
        return user_selected_directory

def try_create_virtual_environment_in_directory(dialog_title: str, directory: str, with_pip:bool = True) -> bool:

    is_safe = is_safe_to_create_directory(dialog_title, directory)

    if is_safe is None or not is_safe:
        exit()

    try:
        venv.create(directory, with_pip=with_pip)
        print(f"Created virtual environment in directory {directory}")

        open_directory_if_desired(dialog_title, directory)

        return True
    except Exception as e:
        print(f"Failed to create virtual environment in directory{directory}: {e}")
        return False

def create_virtual_environment_in_directory_if_desired(dialog_title: str, dialog_message: str, directory: str) -> bool|None:
    do_create_in_user_directory:bool|None = messagebox.askyesnocancel(
        title=dialog_title,
        message=dialog_message,
        detail=directory
    )

    if do_create_in_user_directory is None:
        print(f"User cancelled the operation")
        return None

    if not do_create_in_user_directory:
        print(f"User opted not to create virtual environment in directory: {directory}")
        return False

    return try_create_virtual_environment_in_directory(dialog_title, directory)

def create_virtual_environment_in_user_directory_if_desired(virtual_environment_directory_name:str):
    dialog_message = f"Create virtual environment in user directory?"
    directory = os.path.join(os.path.expanduser("~"), virtual_environment_directory_name)
    created_virtual_environment = create_virtual_environment_in_directory_if_desired(DIALOG_TITLE, dialog_message, directory)

    if created_virtual_environment is None or created_virtual_environment:
        exit()

def create_virtual_environment_in_working_directory_if_desired(virtual_environment_directory_name:str):
    dialog_message = f"Create virtual environment in working directory?"
    directory = os.path.join(os.getcwd(), virtual_environment_directory_name)
    created_virtual_environment = create_virtual_environment_in_directory_if_desired(DIALOG_TITLE, dialog_message, directory)

    if created_virtual_environment is None or created_virtual_environment:
        exit()

def create_virtual_environment_in_selected_directory_if_desired(virtual_environment_directory_name:str):
    dialog_message = f"Select a directory to create the virtual environment in"
    directory = ask_user_to_select_virtual_environment_directory(dialog_message, os.getcwd())

    if directory is None:
        exit()

    directory = os.path.join(directory, virtual_environment_directory_name)
    try_create_virtual_environment_in_directory(DIALOG_TITLE, directory)

virtual_environment_directory_name = ask_user_for_virtual_environment_directory_name(DIALOG_TITLE)
if virtual_environment_directory_name is None:
    exit()

create_virtual_environment_in_user_directory_if_desired(virtual_environment_directory_name)
create_virtual_environment_in_working_directory_if_desired(virtual_environment_directory_name)
create_virtual_environment_in_selected_directory_if_desired(virtual_environment_directory_name)






#
#
#
# venv_dir = os.path.join(os.path.expanduser("~"), ".venv")
# msg = f"Create virtual environment for user? ({venv_dir})?"
# shall = raw_input("%s (Y/N) " %msg).lower() == 'y'
#
# if shall:
#     if os.path.exists(venv_dir):
#
#
#
#     If
# shall:
#
# venv_dir = os.getcwd()
# msg = p”Create
# virtual
# environment in current
# directory? ({venv_dir})”
# shall = raw_input("%s (Y/N) " % msg).lower() == 'y'
#
# python - c
# 'import virtualenv; import os; print("... Creating Virtual Environment (.venv) Run Config Start ..."); venv_dir = os.path.join(os.path.expanduser("~"), ".venv”); if os.path.exists(path); print(“…Creating Virtual Environment (.venv) Run Config End ...");'
#

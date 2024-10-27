import tkinter
from sys import exception
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

import os
import sys
import venv

DIALOG_TITLE = "Create Virtual Environment"

def is_safe_to_create_directory(dialog_title: str, directory: str) -> bool:
    if os.path.exists(directory):
        do_override_existing_directory: bool = messagebox.askyesnocancel(
            title=dialog_title,
            message=f"The directory already exists; override it?",
            detail=directory
        )
        return do_override_existing_directory
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
        print(f"User opted not to set a custom virtual environment directory name")
    else:
        print(f"User set the virtual environment directory name to {user_entered_directory_name}")
        directory_name = user_entered_directory_name

    return directory_name

def ask_user_for_virtual_environment_directory(dialog_title: str, initial_directory: str) -> str | None:
    root = tkinter.Tk()
    root.withdraw() # Hide the main window

    user_selected_directory = filedialog.askdirectory(
        title=dialog_title,
        initialdir=initial_directory
    )

    root.destroy()

    if user_selected_directory is None:
        print(f"User opted not to select a directory")
        return None
    else:
        print(f"User selected directory {user_selected_directory}")
        return user_selected_directory

def try_create_virtual_environment_in_directory(dialog_title: str, directory: str, with_pip:bool = True) -> bool:

    if not is_safe_to_create_directory(dialog_title, directory):
        return False

    try:
        venv.create(directory, with_pip=with_pip)
        print(f"Created virtual environment in directory {directory}")
        return True
    except Exception as e:
        print(f"Failed to create virtual environment in directory{directory}: {e}")
        return False

def create_virtual_environment_in_directory_if_desired(dialog_title: str, dialog_message: str, directory: str) -> bool:
    do_create_in_user_directory:bool = messagebox.askyesnocancel(
        title=dialog_title,
        message=dialog_message,
        detail=directory
    )

    if do_create_in_user_directory:
        return try_create_virtual_environment_in_directory(dialog_title, directory)

    print(f"User opted not to create virtual environment in directory: {directory}")
    return False


virtual_environment_directory_name = ask_user_for_virtual_environment_directory_name(DIALOG_TITLE)

dialog_message = f"Create virtual environment in user directory?"
directory = os.path.join(os.path.expanduser("~"), virtual_environment_directory_name)
created_virtual_environment = create_virtual_environment_in_directory_if_desired(DIALOG_TITLE, dialog_message, directory)

if created_virtual_environment:
    exit()

dialog_message = f"Create virtual environment in working directory?"
directory = os.path.join(os.getcwd(), virtual_environment_directory_name)
created_virtual_environment = create_virtual_environment_in_directory_if_desired(DIALOG_TITLE, dialog_message, directory)

if created_virtual_environment:
    exit()

dialog_message = f"Select a directory to create the virtual environment in"
directory = ask_user_for_virtual_environment_directory(dialog_message, os.getcwd())
if directory is None:
    print(f"User opted not to select a directory")
else:
    print(f"User selected directory {directory}")
    directory = os.path.join(directory, virtual_environment_directory_name)
    try_create_virtual_environment_in_directory(DIALOG_TITLE, directory)









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

import os
from PyOneLiner import OneLiner
from os import system
from tkinter import messagebox

import onelinerizer
#Generate Rung / Debug configurations from the python files

def remove_newlines(content: str) -> str:
    return content.replace("\n", "").replace("\r", "")

def get_file_as_text(filepath: str) -> str:
    with open(filepath, "r") as file:
        file_content = file.read()
        file.close()
    return file_content

def generate_run_debug_configuration(filepath: str):
    # file_as_text = get_file_as_text(filepath)
    # file_text_without_newlines = remove_newlines(file_as_text)
    #
    # file_as_one_line = onelinerizer.onelinerize(file_as_text)
    # print(file_as_one_line)

    oneliner = OneLiner(filepath, type_="python")

    # bytes = oneliner.bytes
    # print(bytes)
    #
    # bytes_str = str(bytes)
    # print(bytes_str)

    oneliner.base64()
    oneline_result = oneliner.done()  # done throws an error if a command was not run (e.g. normal, xor, ascii85, lzma, binary, base16, bz2)
    print(oneline_result)


working_directory = os.getcwd()
filepaths = [r"Shell Script/Virtual Environment/install_virtual_environment.py"]

for filepath in filepaths:
    absolute_filepath = os.path.join(working_directory, filepath)
    exists = os.path.exists(absolute_filepath)

    if not exists:
        messagebox.showerror(
            title="File Not Found",
            message=f"Couldn't create Run/Debug Configuration. File not found at:",
            detail=absolute_filepath
        )
        continue

    print(f"Generating Run/Debug Configuration for {absolute_filepath}")
    generate_run_debug_configuration(absolute_filepath)
    print("Run/Debug Configuration Generated")
    print("\n\n")
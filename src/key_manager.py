#Nicholas Hoven 2025
import os
import pyperclip
from keys_gui import *


def get_file_contents(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents


def get_local_path(data_path, file_name):
    return data_path + "\\" + file_name


def get_key(file_path):
    with open(file_path, 'r') as file:
            contents = file.read()
    return contents


def copy_to_clipboard(text):
    pyperclip.copy(text)


def list_files(directory):
    if directory != "":
        contents = []
        files = os.listdir(directory)
        for file in files:
            contents.append(file)
        # print(file)
        return contents
    

def get_file_paths(directory):  # Gets all of the files in a directory.
    file_paths = []
    files = os.listdir(directory)
    for file in files:
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path):
            file_paths.append(full_path)

    return file_paths


def read_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"An error occurred: {e}"
    

def copy_key(data_path, local_file):
    key_path = get_local_path(data_path, local_file)
    key = get_key(key_path)
    pyperclip.copy(key)


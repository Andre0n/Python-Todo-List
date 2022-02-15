#!/usr/bin/env python3
import sys
import os
import tempfile
from hashlib import md5 as md5

todos_file_path = os.path.join(tempfile.gettempdir(), "toodsdb.txt")

def print_help():
    help_text = """Todo

Usage: todo <command> <argument>

Default commands:
    -h: Print the help.
    -a: Add a new task, eg.: todo -a "some task to do."
    -l: Print all tasks.
    -r: Remove a task, eg.: todo -r <task_code>.
"""
    print(help_text)


def get_task_title(input):
    s = " ".join(input[2::]) # Join all arguments after -a.
    s = " ".join(s.split()) # Remove extra spaces.
    return s


def add_task(input):
    try:
        assert len(input) > 2
        with open(todos_file_path, "a") as file:
            task_title = get_task_title(input)
            task_code = md5(task_title.encode()).hexdigest()
            task = f"{task_code[::5]} : {task_title}\n"
            file.write(task)
    except:
        print("Error: Missing `argument`.\nUse `todo -h` to see the help.")
        sys.exit(1)


def print_list():
    try:
        with open(todos_file_path, "r") as file:
            lines = file.readlines()
            assert (len(lines)) > 0
            for line in lines:
                print(line, end="")
    except FileNotFoundError:
        print("No tasks to print.\nUse `todo -h` to see the help.")
        sys.exit(1)
    except AssertionError:
        print("No tasks to print.\nUse `todo -h` to see the help.")
        sys.exit(1)



def remove_task(input):
    try:
        assert len(input) > 2
        with open(todos_file_path, "r") as file:
            lines = file.readlines()
        with open(todos_file_path, "w") as file:
            for line in lines:
                if line.split()[0] != input [2]:
                    file.write(line)
    except AssertionError:
        print("Error: Missing `argument`.\nUse `todo -h` to see the help.")
        sys.exit(1)
    except FileNotFoundError:
        print("No tasks to remove.\nUse `todo -h` to see the help.")
        sys.exit(1)


def app():
    try:
        input = sys.argv
        assert len(input) > 1
        if input [1] == "-h":
            print_help()
        elif input [1] == "-a":
            add_task(input)
        elif input[1] == "-l":
            print_list()
        elif input[1] == "-r":
            remove_task(input)
        else:
            print("Error: Invalid `command`\nUse `todo -h` to see the help.")
    except AssertionError:
        print("Error: Missing `command`.\nUse `todo -h` to see the help.")
        sys.exit(1)

if __name__ == "__main__":
    app()

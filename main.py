#!/usr/bin/python3
import os
import tempfile
import sys


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

def app():
    try:
        input = sys.argv
        assert len(input) > 1
        if input [1] == "-h":
            print_help()
    except AssertionError:
        print("Error: Missing `command`\nUse todo -h to see the help")
if __name__ == "__main__":
    app()

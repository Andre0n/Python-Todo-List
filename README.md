# Python Todo app 📝

Write down your daily tasks.

## Features

- Add a task.
- List all tasks.
- Remove a task.
- All tasks are saved to disk in the temp folder.

## Running locally

Clone the project

```bash
git clone https://github.com/Andre0n/Python-Todo-List.git
```

Change into the project directory

```bash
cd Python-Todo-List
```

Run Linux/Mac

```bash
python3 ./main.py
```

Run Windows

```bash
py .\main.py
```

## Compiling

Compile Linux

Require ```gcc Cython Python3```

```bash
cp main.py main.pyx
cython -3 --embed -o main.c main.pyx
gcc -I /usr/include/python3.9 -o pytodo main.c -lpython3.9 -lpthread -lm -lutil -ldl
sudo mv pytodo /usr/local/bin/pytodo
```

## Todo

- [ ] Add window and mac compiling section.


## Authors

- [@Andre0n](https://www.github.com/Andre0n)

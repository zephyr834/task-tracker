# Tasksu: A CLI Application to manage tasks.

## Description:

Tasksu is a simple command-line interface (CLI) task management application. It allows the user to add, update, list, and delete tasks and save all data to a JSON file.

This project was built while following the python roadmap:
https://roadmap.sh/projects/task-tracker

Built on:
Python3 - 3.11.9
Mac

## Commands

- `add TITLE DESCRIPTION` : Add a new task
- `delete UID` : Delete a task
- `list` : Lists all tasks
  - Options:
    - `-s, --status TEXT` : Filter tasks by status: todo, in-progress, done
- `mark STATUS UID` : Mark a task with an updated status
- `update UID TITLE` : Update the title or description of task
  - Options:
    - `-d, --description TEXT` : Updates the task description

## Install

```bash
pip3 install git+https://github.com/zephyr834/tasksu
```

## Usage:

- **Add a task**

  ```bash
  $ tasksu add "Pet a cat" "Petting the feline friend"
  $ tasksu list

  |  UID  |             Title             |          Description          |   Status  |           Created At          |           Updated At          |
  |   1   |           Pet a cat           |   Petting the feline friend   |    todo   |   October 02, 2024 03:51 PM   |   October 02, 2024 03:51 PM   |
  ```

- **Update a task**

  ```bash
  $ tasksu update 1 "Pet a dog" -d "Dogs are better."
  $ tasksu list

  |  UID  |             Title             |          Description          |     Status     |           Created At          |           Updated At          |
  |   1   |           Pet a dog           |        Dogs are better.       |      todo      |   October 02, 2024 03:51 PM   |   October 02, 2024 03:57 PM   |
  ```

- **Mark a task in-progress**

  ```bash
  $ tasksu mark in-progress 1
  $ tasksu list

  |  UID  |             Title             |          Description          |     Status     |           Created At          |           Updated At          |
  |   1   |           Pet a dog           |        Dogs are better.       |   in-progress  |   October 02, 2024 03:51 PM   |   October 02, 2024 03:58 PM   |
  ```

- **Mark a task done**

  ```bash
  $ tasksu mark done 1
  $ tasksu list

  |  UID  |             Title             |          Description          |     Status     |           Created At          |           Updated At          |
  |   1   |           Pet a dog           |        Dogs are better.       |      done      |   October 02, 2024 03:51 PM   |   October 02, 2024 03:59 PM   |
  ```

- **List all tasks**

  ```bash
  $ tasksu list

  |  UID  |             Title             |          Description          |     Status     |           Created At          |           Updated At          |
  |   1   |           Pet a dog           |        Dogs are better.       |   in-progress  |   October 02, 2024 03:51 PM   |   October 02, 2024 03:57 PM   |
  |   2   |        Pet a cat again        |          I like cats          |      todo      |   October 02, 2024 04:17 PM   |   October 02, 2024 04:17 PM   |
  ```

- **List all tasks filtered by status**

  ```bash
  $ tasksu list -s todo

  |  UID  |             Title             |          Description          |     Status     |           Created At          |           Updated At          |
  |   2   |        Pet a cat again        |          I like cats          |      todo      |   October 02, 2024 04:17 PM   |   October 02, 2024 04:17 PM   |
  ```

- **Delete a task**

  ```bash
  $ tasksu delete 1
  $ tasksu list

  |  UID  |             Title             |          Description          |     Status     |           Created At          |           Updated At          |
  |   2   |        Pet a cat again        |          I like cats          |      todo      |   October 02, 2024 04:17 PM   |   October 02, 2024 04:17 PM   |
  ```

## Setup source code

The following steps are for cloning, modifying, testing the code.

- Clone

```bash
git clone git@github.com:zephyr834/tasksu.git
cd tasksu
```

- Setup virtual env

```bash
python3 -m venv venv
source ./venv/bin/activate
```

- Install Requirements

```bash
pip3 install -r requirements.txt
```

- Run CLI

```bash
python3 app/main.py [OPTIONS] COMMAND [ARGS]
```

- Run tests

```bash
pytest
```

- Debugging
  If running the tests creates a "ModuleNotFoundError", run the following command in your virtual env.

```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/app
```

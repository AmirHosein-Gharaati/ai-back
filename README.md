# AI Course Project

## Description

TODO

## Installation

Create a python local environment. `venv` is suggested.

```bash
python3 -m venv ./venv
```

Activate the environment

Linux:
```bash
source ./venv/bin/activate
```

Install libraries for the project

```bash
pip3 install -r requirements.txt
```

run project using uvicorn web server:
```bash
uvicorn main:app --reload
```
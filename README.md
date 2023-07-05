# AI Course Project

## Description

TODO

## Installation

Create a python local environment. `venv` is suggested (make sure you have installed `venv` package)

```bash
python3 -m venv ./venv
```

Activate the environment

Linux:
```bash
source ./venv/bin/activate
```

Windows there is an `activate.bat` file in `bin` folder. Run it(not sure about the syntax):

```bash
venv\Scripts\activate
```

Install libraries for the project

```bash
pip3 install -r requirements.txt
```

run project using uvicorn web server:
```bash
uvicorn main:app --reload
```
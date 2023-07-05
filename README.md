# AI Course Project

## Description

This project aims to develop a predictive model for diabetes using logistic regression, a popular machine learning algorithm. The project consists of three phases.

Phase One: Data Preparation
In this phase, the focus is on obtaining and preparing the required data for training and evaluating the logistic regression model. The provided website can be used to gather the data, ensuring it is in a suitable format for training.

Phase Two: Training a Logistic Regression Model for Diabetes Prediction
The second phase involves training the logistic regression model using the prepared data. The data is split into a training set and a validation set. The model is trained on the training set to learn the relationships between input features (e.g., age, BMI, blood pressure, glucose levels) and the target variable (diabetic or non-diabetic). The model's performance is evaluated using the validation set.

Phase Three: Developing a User Interface for Diabetes Prediction
In the third phase, a user interface is developed to allow users to input their features. The trained logistic regression model predicts whether the user is diabetic or non-diabetic based on the provided features.

Note: It is required to implement the logistic regression algorithm without using pre-existing libraries.

Overall, this project aims to develop a logistic regression model for diabetes prediction and provide a user-friendly interface for individuals to assess their likelihood of being diabetic based on their personal features.

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
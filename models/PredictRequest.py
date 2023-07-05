from pydantic import BaseModel


class PredictRequest(BaseModel):
    pregnancies: int
    glucose: float
    bloodPressure: float
    skinThickness: float
    insulin: float
    BMI: float
    diabetesPedigreeFunction: int
    age: int
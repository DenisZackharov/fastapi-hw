from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from pydantic import BaseModel, Field

app = FastAPI()

model = joblib.load('model.pkl')


class Prediction(BaseModel):
    predict: int = Field(
        ...,
        description="Результат предсказания",
    )
    success: bool = Field(False, description="Результат выполнения запроса")


@app.post("/predict")
async def predict(features: list[float]) -> Prediction:
    if len(features) != 4:
        raise HTTPException(status_code=422, detail="Ожидались 4 числа с плавающей точкой")

    input_array = np.array(features).reshape(1, -1)
    prediction = model.predict(input_array)
    return Prediction(predict=prediction[0], success=True)

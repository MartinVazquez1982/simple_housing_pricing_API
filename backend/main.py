from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Cargar modelo entrenado
model = joblib.load("model.pkl")

# Crear instancia de FastAPI
app = FastAPI(title="House Price Predictor API")

# Esquema de entrada con Pydantic
class HouseFeatures(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: int
    sqft_lot: int
    floors: float
    waterfront: int
    view: int
    condition: int
    grade: int
    sqft_above: int
    sqft_basement: int
    yr_built: int
    yr_renovated: int
    zipcode: int
    lat: float
    long: float
    sqft_living15: int
    sqft_lot15: int

@app.post("/predict")
def predict_price(features: HouseFeatures):
    # Convertir datos de entrada a array
    input_data = np.array([[
        features.bedrooms, features.bathrooms, features.sqft_living,
        features.sqft_lot, features.floors, features.waterfront,
        features.view, features.condition, features.grade,
        features.sqft_above, features.sqft_basement,
        features.yr_built, features.yr_renovated, features.zipcode,
        features.lat, features.long, features.sqft_living15,
        features.sqft_lot15
    ]])

    # Realizar predicción
    predicted_price = model.predict(input_data)[0]

    return {"predicted_price": predicted_price}

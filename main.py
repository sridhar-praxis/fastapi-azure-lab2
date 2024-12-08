from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model
with open("slr_model.pkl", "rb") as f:
    model = pickle.load(f)

# Initialize FastAPI app
app = FastAPI()

# Pydantic model for request body
class PredictRequest(BaseModel):
    x: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Simple Linear Regression API v2"}

@app.post("/predict/")
def predict(request: PredictRequest):
    # Predict using the loaded model
    x_reshaped = np.array([[request.x]])
    prediction = model.predict(x_reshaped)[0]
    return {"input": request.x, "prediction": prediction}

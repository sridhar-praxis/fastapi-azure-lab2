# myapp_fastapi_fit.py

import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Define the data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 3, 5, 8, 11])

# Create the model
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Save the model as a pickle file
with open("slr_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")

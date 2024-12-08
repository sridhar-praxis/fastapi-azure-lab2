# Use an official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI application files to the container
COPY main.py /app/
COPY slr_model.pkl /app/

# Install necessary dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

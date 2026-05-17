# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the necessary files into the container
COPY Diabetes-Prediction-System.py ./
COPY trained_model.sav ./

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit","run","Diabetes-Prediction-System.py","--server.port=8501","--server.address=0.0.0.0"]
FROM python:3.8-slim-buster

COPY requirements.txt app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "fastapiapp:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# # Use the official Python 3.10 base image
# FROM python:3.10

# # Set the working directory in the container
# WORKDIR /code

# # Copy the requirements.txt file into the container
# COPY ./requirements.txt /code/requirements.txt

# # Install Python dependencies
# RUN pip install -r /code/requirements.txt

# RUN apt-get update && apt-get install -y build-essential

# # Copy the FastAPI app file into the container

# COPY ./fastapiapp.py /code/fastapiapp.py

# # Copy any required model files (e.g., .pkl files)
# COPY ./scaler.pkl /code/scaler.pkl
# COPY ./type.pkl /code/type.pkl

# # Expose the default port used by FastAPI
# EXPOSE 80

# # Run the FastAPI app using Uvicorn
# CMD ["uvicorn", "fastapiapp:app", "--host", "0.0.0.0", "--port", "80"]

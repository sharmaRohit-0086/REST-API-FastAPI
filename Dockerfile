# Use the official image as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 80 available to the world outside this container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]


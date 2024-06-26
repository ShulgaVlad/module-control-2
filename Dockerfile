# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Copy .env file to the container
COPY .env .env

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the command to start the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

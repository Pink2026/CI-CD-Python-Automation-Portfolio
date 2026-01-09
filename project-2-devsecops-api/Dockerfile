FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the local code into the container's working directory
COPY . .

# Install dependencies 
RUN pip install --no-cache-dir flask

# Inform Dcker that the container listens on port 5000
EXPOSE 5000

# The command to start the appliction
CMD ["python", "app.py"]
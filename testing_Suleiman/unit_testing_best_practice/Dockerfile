# Use a more recent and lightweight Python image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy only necessary files to avoid unnecessary layers
COPY requirements.txt /app/
COPY src/validators.py /app/src/
COPY test/test_validators.py /app/test/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Run the tests using pytest
CMD ["pytest", "src/validators.py","test/test_validators.py"]

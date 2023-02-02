# Use a base image with Python and the required dependencies
FROM python:3.9-alpine

# Copy the backend code and the requirements file into the container
COPY . /app
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Set environment variables for the connection string
ENV DATABASE_URL postgresql://postgres:19990521a@db:5432/nameInfo

EXPOSE 5000

# Start the backend server
CMD ["flask", "run", "--host=0.0.0.0"]
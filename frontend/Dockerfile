# Use an existing Docker image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the frontend code to the container
COPY . .

# Build the React frontend
RUN npm run build

# Set the environment variable for the base URL of the backend
ENV REACT_APP_BASE_URL=http://172.19.0.3:5000/

# Start the frontend
CMD ["npm", "start","--host=0.0.0.0"]

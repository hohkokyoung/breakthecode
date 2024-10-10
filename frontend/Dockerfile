# Use the official Node.js image as the base image
FROM node:14 AS build

# Set the working directory
WORKDIR /frontend

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application for production
RUN npm run build

# Use Nginx to serve the React app
FROM nginx:alpine

# Copy the build files from the previous stage
COPY --from=build /frontend/build /usr/share/nginx/html

# Expose the port on which the app runs
EXPOSE 80

# Command to run the server
CMD ["nginx", "-g", "daemon off;"]
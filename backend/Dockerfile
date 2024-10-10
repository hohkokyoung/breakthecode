FROM python:3.11.4-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install system dependencies
RUN apt-get update && apt-get install -y netcat git

# Set the working directory
WORKDIR /usr/src/backend

# Copy requirements.txt first to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/backend/entrypoint.sh
RUN chmod +x /usr/src/backend/entrypoint.sh

# Copy the rest of the application code
COPY . .

# Run migrations (if necessary)
# RUN python manage.py migrate

# Expose the port on which the Django app runs
EXPOSE 8000

# run entrypoint.sh
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]
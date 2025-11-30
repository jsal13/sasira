FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY viewer/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the working directory to viewer for the Flask app
WORKDIR /app/viewer

# Expose the port
EXPOSE 8001

# Set environment variables
ENV FLASK_APP=server.py
ENV FLASK_ENV=development

# Run the Flask application
CMD ["python", "server.py"]
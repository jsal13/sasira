# Sasiran Docker Setup

## Quick Start

### Using Docker Compose (Recommended)
```bash
# Build and run the container
docker-compose up --build

# Run in background
docker-compose up -d --build
```

### Using Docker directly
```bash
# Build the image
docker build -t sasira-viewer .

# Run the container
docker run -p 8001:8001 sasira-viewer
```

## Access the Application
Open your browser and go to: http://localhost:8001

## Development Mode
The Docker setup includes:
- Hot reload enabled
- Source files mounted as read-only volumes
- Automatic restart on failure

## Stopping the Application
```bash
# If using docker-compose
docker-compose down

# If using docker directly
docker stop <container_id>
```

## Building for Production
For production, modify the Dockerfile to:
1. Set `FLASK_ENV=production`
2. Remove debug mode
3. Use a production WSGI server like Gunicorn
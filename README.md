# Audio Processing Website

### Project Overview

This project is a Flask-based web application designed to handle audio file uploads and process them using a custom data processing pipeline. The application enables users to record, upload, and process audio files, with the output being a transcription or some other derived result from the processing pipeline.

### Features

- **Audio File Upload**: Supports uploading of .wav and .mp3 audio files.

- **Audio Recording**: Users can record audio directly in the frontend and submit it for processing.

- **Audio Processing**: Integrates a customizable DataProcessingPipeline to process the uploaded or recorded audio files.

- **API Endpoints**: Provides RESTful API endpoints for saving and processing audio files.

## Prerequisites

- Python 3.9+
- Docker and Docker Compose (for containerized deployment)

## Installation

### Local Development

1. Clone the repository:
````bash
git clone https://github.com/Vampaxx/Speech_2_Text
cd Speech_2_Text
````
2. Create a virtual environment and install dependencies:

Make sure you have Python and pip installed. Then install the required dependencies:

```bash

pip install -r requirements.txt
```

3. Start the Flask application:
````bash
flask run
````
The application will be available at http://127.0.0.1:5000.

### Using Docker Compose

1. Build and start the application using Docker Compose:
````bash
docker-compose up --build
````
2.Access the application at http://localhost:5000.



## Directory Structure
```plaintext
project-directory/
|── app.py               # Flask application
|── requirements.txt    # Project dependencies
|── Dockerfile          # Docker image setup
|── docker-compose.yml  # Docker Compose setup
|__ Static
  |__ css
  |__ js
  |__ transcription
  |__ uploads           # Directory for uploaded files
````

### Customization

Pipeline Integration: Replace the DataProcessingPipeline class in app.py with your custom logic. The pipeline's main() method should accept the audio file path and return the desired output.

Frontend Integration: Customize the frontend code located in the static directory for tailored user experience.

### Deployment

Use the provided Dockerfile to containerize the application.

Deploy the container to your preferred cloud provider (e.g., AWS, Google Cloud, Azure, etc.).

Configure a reverse proxy (e.g., Nginx) for production deployment.


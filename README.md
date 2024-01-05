## Getting Started

Follow these steps to run the project.

## Prerequisites

Before running the project, make sure to create a .env file in the root directory with the following content:

OPENAI_API_KEY=your_openai_api_key

GOOGLE_AI_API_KEY=your_google_ai_api_key

Replace your_openai_api_key and your_google_ai_api_key with the actual API keys you obtain from OpenAI and Google AI.

## Clone the repository using the following command:

git clone "url"

## Install the project dependencies:

pip install -r requirements.txt

## Running the Application

Start the FastAPI application with the following command:

uvicorn main:app --reload

The application will be accessible at <strong>http://127.0.0.1:8000/docs<strong> once it starts successfully.


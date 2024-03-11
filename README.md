# Gemini Story App - Flask

## Description

The Gemini Story App is a web application that combines the power of generative AI with user-provided image to create inspiring and imaginative stories. Built using Flask, Python, and various web technologies, this app allows users to upload an image and receive an inspiring story generated by the Gemini AI.

## Features

- Image-to-Story Generation:
    - Users upload their own image in supported formats (e.g., JPEG, PNG) directly through the web interface.
    - The app uses the Gemini API (Gemini Pro Vision AI model) to analyze the visual content of the image.
    - Based on the image analysis, it dynamically generates a short story.
- Integration with Gemini AI:
    - The Gemini Pro Vision AI model provides insights into the image.
    - The app combines this information with creative storytelling to produce unique narratives.
- User Experience:
    - A clean and intuitive user interface allows seamless interaction.
    - Users receive instant feedback with their story from the image they choose.

## Technologies Used

- Flask
- Python
- HTML/CSS/JavaScript
- Bootstrap
- Google AI Studio
- Gemini API

## Getting Started

### Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip install -r requirements.txt.

### Configuration

To use the Gemini API, follow these steps:

1. Obtain an API key from the Google AI Studio.
2. Create a `.env` file in the project root folder.
3. Inside the `.env` file, define an environment variable named `GEMINI_API_KEY` and assign your obtained API key to it.

### Run the App

1. Naviagte to the `src` folder.
2. Run the Flask app using `flask run`.
3. Open your web browser and navigate to `http://127.0.0.1:5000`.

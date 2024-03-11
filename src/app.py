import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, url_for
from pathlib import Path
import google.generativeai as genai

app = Flask(__name__)

# Load Gemini API Key from environment variables
load_dotenv()
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

def allowed_file(filename):
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS

# routes
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle image upload
        uploaded_image = request.files["image"]
        if not uploaded_image or not allowed_file(uploaded_image.filename):
            return "Invalid image file. Please select a valid image."

        # Convert the image_path to a Path object
        image_path = Path(os.path.join("static", "images/uploaded_image.jpeg"))
        uploaded_image.save(image_path)

        # Use the exists() method on the Path object
        if not image_path.exists():
            return "Error saving the uploaded image."

        # Process the image using the Gemini API and extract features
        image_parts = [
            {"mime_type": "image/jpeg", "data": image_path.read_bytes()}
        ]

        prompt_parts = [
            "Would you be able to write a short, inspiring story based on this image I have?\n",
            image_parts[0],
            "\n",
        ]

        response = model.generate_content(prompt_parts)
        generated_story = response.text

        # Use the url_for function to generate the image_url
        image_url = url_for("static", filename="images/uploaded_image.jpeg")

        return render_template("index.html", user_image=image_url, generated_story=generated_story)

    return render_template("index.html")

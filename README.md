# CalorEase

## Overview
In today's fast-paced world, keeping track of calorie intake is vital for maintaining a healthy lifestyle. With rising awareness of diet and nutrition, knowing the caloric value and macronutrient breakdown of foods we consume is essential. Despite this, many people overlook the importance of monitoring their calorie intake, which can lead to unhealthy eating habits and, ultimately, health issues. This project aims to make calorie tracking more accessible by providing an easy-to-use application that recognizes food items and provides detailed nutritional information, along with estimates for the time required to burn those calories through different activities.

## Project Description
This is a Full-Stack Django application designed to help users identify food items and provide detailed caloric and macronutrient information. Users can either search for a specific food item that is passed to an LLM or upload an image of their food. The application uses a finetuned InceptionV3 model to classify the food (20 classes) from the uploaded image. Additionally, it calculates the time required to burn the calories for that food through various physical activities like cycling, running, swimming, and gym workouts.

## Key Features
1. **Search Food**: Users can search for any food item by name. The query is sent to the Chat-Groq chat model utilizing the Llama 3.1 70B LLM, which provides nutritional information, including the caloric value and macronutrients for the selected food.

2. **Classify Food**: Users can upload an image of their food. The finetuned InceptionV3 model identifies the food item, and then the application retrieves the caloric and nutritional details using the Chat-Groq chat model. 

3. **Calorie Burn Time Calculation**: For each food item, the application calculates how long it would take to burn the provided calories through different activities: Cycling, Swimming, Jogging, and Gym workouts. This personalized insight motivates users to stay active and make informed dietary choices.

## Requirements
- **Languages**: Python
- **Libraries**:
  - `tensorflow`
  - `langchain`
  - `langchain-groq`
  - `pillow`
  - `numpy`
  - `humanize`
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django
- **API Key**: Chat-Groq API key
- **Model Files**: Download from Drive Link

## Model Files
Due to size limitations, model files are not included in this repository. 

### Download Instructions
Download the model files from the following links:
   - Model Files (173MB): [Download from Google Drive](https://drive.google.com/drive/folders/1xyhAtGVIy9vxcYW4Jo0fm7kijxYIIQqW?usp=sharing)
   - Place the downloaded files in the following directory structure:
   - classify/`model`

## Getting Started
1. **Download Files**:
   - Clone the repository from Github.
   - Download the Model Files.
1. **Set Up Environment**:
   - Create a virtual environment using Conda or Python.
   - Install required packages: 
     ```bash
     pip install -r requirements.txt
     ```
2. **Run the Application**:
   - Replace 'GROQ_API_KEY' in counter/views.py with your Chat-Groq API KEY.
   - Start the server:
     ```bash
     python manage.py runserver
     ```
3. **Download the Dataset**:
   - Dataset link: (https://www.kaggle.com/datasets/theeyeschico/indian-food-classification)

## Usage
Once the server is running, open the web application in your browser. You can either search for a food item by name or upload an image to classify it. On the results page, you’ll see:
- Caloric value and macronutrient breakdown of the food item per 100 grams.
- Estimated time to burn the calories through various activities like cycling, swimming, jogging, and gym workouts.

### Bugs and Fixes
If you encounter any bugs or have suggestions for improvements, please feel free to reach out at:
`a.bhagyacharan@gmail.com`

# counter/views.py
from django.conf import settings
from django.shortcuts import render
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def home(request):
    api = None
    
    # Handle both POST requests and GET requests with food parameter
    if request.method == 'POST':
        food_item = request.POST['query']
    else:
        food_item = request.GET.get('query')
        
    # Process the food_item if we have one from either POST or GET
    if food_item:
        # Your existing nutrition processing code
        nutrition_prompt = f'''
        Provide detailed nutritional information for {food_item} per 100 grams.
        Return the response as a JSON array containing a single object with these exact fields and format:

        [{{
            "name": "{food_item}",
            "calories": <number or "Not available">,
            "serving_size_g": <number or "Not available">,
            "fat_total_g": <number or "Not available">,
            "fat_saturated_g": <number or "Not available">,
            "protein_g": <number or "Not available">,
            "sodium_mg": <number or "Not available">,
            "potassium_mg": <number or "Not available">,
            "cholesterol_mg": <number or "Not available">,
            "carbohydrates_total_g": <number or "Not available">,
            "fiber_g": <number or "Not available">,
            "sugar_g": <number or "Not available">,
        }}]

        Important:
        1. Return ONLY the JSON array, no additional text
        2. Use exact field names as shown
        3. Values should be numbers when available
        4. Use "Not available" for unknown values
        5. Make sure the response is valid JSON
        '''

        # Initialize the Groq chat model
        chat = ChatGroq(
            api_key=os.getenv('GROQ_API_KEY'),
            model_name="llama-3.1-70b-versatile",
            temperature=0.1
        )
        
        try:
            messages = [
                HumanMessage(content=nutrition_prompt)
            ]
            
            response = chat.invoke(messages)
            
            try:
                api = json.loads(response.content)
                if not isinstance(api, list):
                    api = [api]
            except json.JSONDecodeError:
                api = [{
                    "name": food_item,
                    "error": "Failed to parse nutrition data",
                    "status": "error"
                }]
            
            print(json.dumps(api, indent=2))
            
        except Exception as e:
            api = [{
                "name": food_item,
                "error": "oops! There was an error",
                "details": str(e),
                "status": "error"
            }]
            print(e)
    
    # Render the template with results (if any)
    context = {'api': api} if api else {'query': 'Enter a valid query'}
    return render(request, 'home.html', context)
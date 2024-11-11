# classify views.py

from django.shortcuts import render
from django.http import JsonResponse
from .model.model_loader import ImageClassifier
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect ###
from django.urls import reverse ###
import numpy as np
from PIL import Image
import io
import logging

logger = logging.getLogger(__name__)

def upload_page(request):
    return render(request, 'upload.html')

@csrf_exempt
def predict_image(request):
    if request.method == 'POST':
        try:
            if 'image' not in request.FILES:
                    return JsonResponse({
                        'success': False,
                        'error': 'No image file provided'
                    })
            
            image_file = request.FILES['image']

            try:
                image = Image.open(io.BytesIO(image_file.read()))
                if image.format not in ['JPEG', 'PNG']:
                    return JsonResponse({
                        'success': False,
                        'error': 'Unsupported image format. Please use JPEG or PNG.'
                    })
            except Exception as e:
                return JsonResponse({
                    'success': False,
                    'error': 'Invalid image file'
                })
            
            # Get prediction
            prediction = ImageClassifier.predict(image)

            if isinstance(prediction, np.ndarray):
                prediction = prediction.tolist()
            
            return JsonResponse({
                'success': True,
                'prediction': prediction,
                'redirect_url': f'/foodie/?query={prediction}'  # Absolute URL path
            })
        
        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    
    return JsonResponse({
        'success': False,
        'error': 'Only POST requests are allowed'
    })
from django.shortcuts import render
# from tensorflow.keras.applications.resnet50 import ResNet50
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from rest_framework.decorators import api_view

# from  tensorflow.keras.models import load_model
# import numpy as np
import json
import base64
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from io import BytesIO
import io
from PIL import Image



# Create your views here.

# model =load_model('restnetmodel')


@api_view(['POST'])
def predict(request):
    if request.method=='POST':
        data = JSONParser().parse(request)

        im_b64=data['image']

        # convert it into bytes  
        img_bytes = base64.b64decode(im_b64.encode('utf-8'))

        # convert bytes data to PIL Image object
        image = Image.open(io.BytesIO(img_bytes))
        image.save('client.jpg')
        print(image)
        
        # preds = model.predict(image)

        # predictions=decode_predictions(preds, top=10)[0]
        # prediction_dictionary={item[1]:item[2] for item in predictions}

    return HttpResponse('got data')






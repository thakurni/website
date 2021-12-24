from rest_framework.decorators import api_view
from django.shortcuts import render


from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
from  tensorflow.keras.models import load_model


import json
import base64
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from io import BytesIO
import io
from PIL import Image

model=load_model('restnetmodel')


@api_view(['POST'])
def predict(request):
    if request.method=='POST':
        data = JSONParser().parse(request)

        im_b64=data['image']

        # convert it into bytes  
        img_bytes = base64.b64decode(im_b64.encode('utf-8'))

        # convert bytes data to PIL Image object
        recovered_image= Image.open(io.BytesIO(img_bytes))


        
        x = image.img_to_array(recovered_image.resize((224,224)))
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        x = model.predict(x)
        predictions=decode_predictions(x, top=10)[0]
        prediction_list={item[1]:item[2] for item in predictions}
        
        return HttpResponse(prediction_list)


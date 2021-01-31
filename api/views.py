from django.shortcuts import render
from django.http import JsonResponse
# Third Party imports:
# APi response
# from pathlib import Path
import os
import cv2
from rest_framework.response import Response
# django rest framework api wrapper
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage

from . import ocr

from rest_framework.viewsets import ViewSet
from .serializers import ImgFileSerializer

# BASE_DIR = Path(__file__).resolve().parent.parent
# MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')

# ViewSets define the view behavior.
class OcrView(ViewSet):
    serializer_class = ImgFileSerializer

    def list(self, request):
        return Response("Its a GET request try making a POST request")

    def create(self, request):
        img = request.FILES.get('img')
        fs=FileSystemStorage()
        name=fs.save(img.name,img)
        path=os.path.join('media',name)
        img=cv2.imread(path)
        response={"Image":name,"Text":ocr.ocr(img)}
        return Response(response)




# def demo_view(request):
#     data={
#         "Name":"Vaibhav Haswani",
#         "Age":"12"
#     }
#     return JsonResponse(data)

#Class base demo view

# class DemoView(APIView):
#     def get(self,request,*args,**kwargs):
#         data = {
#             "Name": "Vaibhav Haswani",
#             "Age": "12"
#         }
#         print(request.file)
#         return Response(data)
#     def post(self,request,*args,**kwargs):
#         data = {
#             "Name": "Vaibhav Haswani",
#             "Age": "12"
#         }
#         print(request.data['file'])
#         return Response(data)

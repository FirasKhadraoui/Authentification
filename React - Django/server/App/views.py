from lib2to3.pgen2 import token
from tokenize import Triple
from urllib import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

from App.models import *
from App.serializers import *

from django.core.files.storage import default_storage

import datetime as dt
import pandas as pd
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

 #######################################      PROJECT        ##########################################
@csrf_exempt
def projectApi(request,id=0):
    if request.method=='GET':
        projects = Project.objects.all()
        projects_serializer=ProjectSerializer(projects,many=True)
        return JsonResponse(projects_serializer.data,safe=False)
    elif request.method=='POST':
        project_data=JSONParser().parse(request)
        projects_serializer=ProjectSerializer(data=project_data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        project_data=JSONParser().parse(request)
        project=Project.objects.get(ProjectId=project_data['ProjectId'])
        projects_serializer=ProjectSerializer(project,data=project_data)
        if projects_serializer.is_valid():
            projects_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        project=Project.objects.get(ProjectId=id)
        project.delete()
        return JsonResponse("Deleted Successfully",safe=False)

 
def Import_csv(request):
    print('s')               
    try:
        if request.method == 'POST' and request.FILES['myfile']:
          
            myfile = request.FILES['myfile']        
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            excel_file = uploaded_file_url
            print(excel_file) 
            empexceldata = pd.read_csv("."+excel_file,encoding='utf-8')
            print(type(empexceldata))
            dbframe = empexceldata
            for dbframe in dbframe.itertuples():
                 
              #  fromdate_time_obj = dt.datetime.strptime(dbframe.DOB, '%d-%m-%Y')
                obj = Etudiant.objects.create(EtudiantClass=dbframe.CODE_CL,EtudiantName=dbframe.nom)
                obj.save()
                print(dbframe.nom)

 
            return render(request, 'importexcel.html', {
                'uploaded_file_url': uploaded_file_url
            })
    except Exception as identifier:            
        print(identifier)
     
    return render(request, 'importexcel.html',{})

 #######################################      USER        #############################################

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None: 
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response =  Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt':token,
            'name':user.name,
            'email':user.email,
            'password':user.password,
            
        }
        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthentificated')
        try:
            payload = jwt.decode(token,'secret',algorithms= ['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthentificated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class logoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'success'
        }
        return response
from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
# from bongRestApi.serializers import UserProfileSerializer

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


# Create your views here.

class UserProfileList(viewsets.ModelViewSet):
    
    # def get(self, request):
    #     userProfile = userProfile.objects.all()
    #     serializers = userProfileSerializers(userProfile, many = True)
    #     return Response(serializers.data)
    
    # def post(self):
    #     pass
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]
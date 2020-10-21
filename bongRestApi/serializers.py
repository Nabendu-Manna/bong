from django.contrib.auth.models import User, Group
from rest_framework import serializers, status
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'first_name', 'last_name', 'email')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required = True)
    # userId = User.id
    class Meta:
        model = UserProfile
        fields = ['user', 'userName', 'image', 'admin']
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data = user_data)
        profile, created = UserProfile.objects.update_or_create(user = user, subject_major = validated_data.pop('subject_major'))
        return profile
    
class PostSerializer(serializers.HyperlinkedModelSerializer):
    userProfile = UserProfileSerializer(required = True)
    userProfile = UserProfile.id
    class Meta:
        model = Post
        fields = ['userProfile', 'postDate', 'name', 'image', 'description']
    
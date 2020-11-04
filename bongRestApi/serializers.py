from django.contrib.auth.models import User, Group
from rest_framework import serializers, status
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'first_name', 'last_name', 'email')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(required = True)
    # user = User
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
    
    # getLikes = getLikes()
    
    class Meta:
        model = Post
        fields = ['userProfile', 'postDate', 'name', 'image', 'description', 'getLikes']
    
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    # post = PostSerializer(required = True)
    post = Post.id
    # userProfile = UserProfileSerializer(required = True)
    userProfile = UserProfile.id

    class Meta:
        model = Comment
        fields = ['post', 'text', 'userProfile', 'date']
        

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    post = Post.id
    userProfile = UserProfile.id
    
    class Meta:
        model = Like
        fields = ['post', 'userProfile', 'status', 'date']
        
class ShareSerializer(serializers.HyperlinkedModelSerializer):
    post = Post.id
    userProfile = UserProfile.id
    
    class Meta:
        model = Share
        fields = ['post', 'userProfile', 'media', 'date']
        
class FollowSerializer(serializers.HyperlinkedModelSerializer):
    post = Post.id
    userProfile = UserProfile.id
    followUser = UserProfile.id
    
    class Meta:
        model = Follow
        fields = ['userProfile', 'followUser', 'date']
        


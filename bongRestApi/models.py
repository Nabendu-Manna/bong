from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, null = True, blank= True, on_delete=models.CASCADE)
    userName = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    admin = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.userName
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def followers(self):
        followers = self.follow.filter(follower = self.user).count()
        return followers
    
    @property
    def followings(self):
        followings = self.follow.filter(following = self.user).count()
        return followings

class Post(models.Model):
    postDate = models.DateTimeField(auto_now_add=True)
    userProfile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def getLikes(self):
        likes = self.like.filter(status = True).count()
        return likes
        
    @property
    def getDislikes(self):
        dislikes = self.like.filter(status = False).count()
        return dislikes
        
    @property
    def getComments(self):
        comments = self.comment_set.count()
        return comments
    
    @property
    def getShares(self):
        shares = self.share_set.count()
        return shares

class Comment(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    userProfile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.text

class Like(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    userProfile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    status = models.BooleanField(default = False)  #True for like and False for dislike
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status

class Share(models.Model):
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    userProfile = models.ForeignKey(UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    media = models.CharField(max_length=50, default = False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.media

class Follow(models.Model):
    userProfile = models.ForeignKey(UserProfile, null=True, blank=True, related_name = 'userProfile', on_delete=models.CASCADE)
    followUser = models.ForeignKey(UserProfile, null=True, blank=True, related_name = 'followUser', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.date


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Member(models.Model):
    user = models.OneToOneField(User, null = True, blank= True, on_delete=models.CASCADE)
    admin = models.BooleanField(default = False)
    userName = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    
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
    def getFollowers(self):
        followers = self.follow.filter(follower = self).count()
        return followers
    
    @property
    def getFollowings(self):
        followings = self.follow.filter(following = self).count()
        return followings

class Post(models.Model):
    postDate = models.DateTimeField(auto_now=True, auto_now_add=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.CharField(max_length=200, blank=True, null=True)
    # like = models.IntegerField(default = 0, null=True, blank = True)
    # dislike = models.IntegerField(default = 0, null=True, blank = True)
    # share = models.IntegerField(default = 0, null=True, blank = True)

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
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    text = models.CharField(max_length=150, blank=True, null=True)

    # class Meta:
    #     verbose_name = _("Comment")
    #     verbose_name_plural = _("Comments")

    def __str__(self):
        return self.text

    # def get_absolute_url(self):
    #     return reverse("Comment_detail", kwargs={"pk": self.pk})

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    status = models.BooleanField(default = False)  #True for like and False for dislike
    date = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __str__(self):
        return self.status

class Share(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    media = models.models.CharField(max_length=50, default = False)
    date = models.DateTimeField(auto_now=True, auto_now_add=True)
    

    # class Meta:
    #     verbose_name = _("Share")
    #     verbose_name_plural = _("Shares")

    def __str__(self):
        return self.media

    # def get_absolute_url(self):
    #     return reverse("Share_detail", kwargs={"pk": self.pk})

class Follow(models.Model):
    follower = models.OneToOneField(Member, on_delete=models.CASCADE)
    following = models.OneToOneField(Member, on_delete=models.CASCADE)
    Synergy = models.IntegerField(default = 0)

    def __str__(self):
        return self.name


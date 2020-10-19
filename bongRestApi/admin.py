from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Customer)
admin.site.register(UserProfile)

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Share)
admin.site.register(Follow)
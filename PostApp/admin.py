from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Pseudo_User)
admin.site.register(Post)
admin.site.register(Post_comments)
admin.site.register(UserProfile)
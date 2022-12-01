from django.contrib import admin
from .models import UserBase

# adds custom user model to the admin panel
admin.site.register(UserBase)

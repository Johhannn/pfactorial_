from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Review

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Review)
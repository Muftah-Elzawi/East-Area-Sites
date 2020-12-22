from django.contrib import admin
from .models import Eastsites
# Register your models here.

admin.site.site_header = "East Sites Admin"
admin.site.site_title = "East Sites Admin Area"
admin.site.index_title = "Welcome to the East Sites admin area"

admin.site.register(Eastsites)

from django.contrib import admin
from user_app.models import  UserDetails,ActivityPeriod

# Register your models here.

#Here we are Registring the model to the django admin 
admin.site.register(UserDetails)
admin.site.register(ActivityPeriod)



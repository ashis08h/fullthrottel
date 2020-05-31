#Importing requied class and methods
from django.db import models

# Create your models here.

#This Model is Used to store the user information in database fields of this model are real name and tz(time zone)
class UserDetails(models.Model):

	real_name = models.CharField(max_length=100)
	tz = models.CharField(max_length = 100)

	def __str__(self):
		return self.real_name

#This Model is used to store the activity of the user into the database fields of the model are user_id , start_time and end_time
class ActivityPeriod(models.Model):	
	user_id = models.ForeignKey(UserDetails,related_name='activity_periods', on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()


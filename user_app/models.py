from django.db import models

# Create your models here.


class UserDetails(models.Model):
	real_name = models.CharField(max_length=100)
	tz = models.CharField(max_length = 100)

	def __str__(self):
		return self.real_name


class ActivityPeriod(models.Model):
	user_id = models.ForeignKey(UserDetails,related_name='activity_periods', on_delete=models.CASCADE)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()


#Importing requied class and methods
from rest_framework import serializers
from user_app.models import UserDetails,ActivityPeriod



#Using UserDetailsSerializers we are serializing and deserializing the UserDetails model data

class ActivityPeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time','end_time']

#Using ActivityPeriodSerializers we are serializing and deserializing the ActivityPeriod model data
class UserDetailsSerializers(serializers.ModelSerializer):


	activity_periods = ActivityPeriodSerializers(many=True, read_only=True)
	class Meta:
		model = UserDetails
		fields = ['id','real_name', 'tz','activity_periods']



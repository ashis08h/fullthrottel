from rest_framework import serializers
from user_app.models import UserDetails,ActivityPeriod



class ActivityPeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time','end_time']


class UserDetailsSerializers(serializers.ModelSerializer):
	activity_periods = ActivityPeriodSerializers(many=True, read_only=True)
	class Meta:
		model = UserDetails
		fields = ['id','real_name', 'tz','activity_periods']



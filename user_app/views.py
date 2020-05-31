from user_app.models import UserDetails,ActivityPeriod
from user_app.serializers import UserDetailsSerializers,ActivityPeriodSerializers
from rest_framework import viewsets
from django.http import HttpResponse
from faker import Faker



class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializers


def population(request):
	fakegen=Faker()
	user_person=['Egon Spengler', 'Glinda Southgood','Joshua Mason','Ashish Kumar'] 
	for item in user_person:
		fake_start_time=fakegen.date_time()
		fake_end_time=fakegen.date_time()
		fake_country=fakegen.timezone()
		try:
			user_details=UserDetails.objects.get(real_name = item)

		except UserDetails.DoesNotExist:
			user_details=UserDetails(real_name = item,tz = fake_country)
			user_details.save()
		popactivity=ActivityPeriod(user_id=user_details,start_time=fake_start_time, end_time=fake_end_time)
		popactivity.save()
	return HttpResponse("your database is populated with dumy data.")


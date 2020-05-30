from user_app.models import UserDetails,ActivityPeriod
from user_app.serializers import UserDetailsSerializers,ActivityPeriodSerializers
from rest_framework import viewsets
from django.http import HttpResponse



class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializers

def population(request):
	import os
	os.environ.setdefault("DJANGO_SETTINGS_MODULE",'user_api.settings')
	import django
	django.setup()
	import random
	from user_app.models import UserDetails,ActivityPeriod
	from faker import Faker
	fakegen=Faker()
	user_person=['Egon Spengler', 'Glinda Southgood','Joshua Mason'] 
	def add_user_person():
		t=UserDetails.objects.get_or_create(real_name=random.choice(user_person))[0]
		t.save()
		return t
	def populate(N=5):
		for entry in range(N):
			user_per=add_user_person()
			fake_country=fakegen.timezone()
			fake_start_time=fakegen.date_time()
			fake_end_time=fakegen.date_time()
			if len(UserDetails.objects.filter(real_name = user_per)) == 1 :
				print(UserDetails.objects.filter(real_name = user_per))
				print(len(UserDetails.objects.filter(real_name = user_per)))
				print(user_per)
				popuser=UserDetails.objects.get_or_create(real_name=user_per)[0]
				popactivity=ActivityPeriod.objects.get_or_create(user_id=popuser,start_time=fake_start_time, end_time=fake_end_time)[0]
			else:
				user_per=add_user_person()
				popuser=UserDetails.objects.get_or_create(real_name=user_per,tz=fake_country)[0]
				popactivity=ActivityPeriod.objects.get_or_create(user_id=popuser,start_time=fake_start_time, end_time=fake_end_time)[0]
			
	populate(3)
	return HttpResponse("your database is populated with dumy data.")


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'user_api.settings')
import django
django.setup()
import random
from user_app.models import UserDetails,ActivityPeriod
from faker import Faker
fakegen=Faker()
def populate(N=5):
	for entry in range(N):
		fake_name=fakegen.name()
		fake_country=fakegen.timezone()
		fake_start_time=fakegen.date_time()
		fake_end_time=fakegen.date_time()
		popuser=UserDetails.objects.get_or_create(real_name=fake_name, tz=fake_country)[0]
		popactivity=ActivityPeriod.objects.get_or_create(user_id=popuser,start_time=fake_start_time, end_time=fake_end_time)[0]
if __name__=='__main__':
	print("populating database")
	populate(3)
	print("COMPLETE!")
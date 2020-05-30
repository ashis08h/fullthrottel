from user_app.models import UserDetails,ActivityPeriod
from user_app.serializers import UserDetailsSerializers,ActivityPeriodSerializers
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializers

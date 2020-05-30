from django.urls import path,include
from user_app.views import UserViewSet
from user_app import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user_details', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('populate/data/', views.population, name='population'),
]

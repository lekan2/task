from django.urls import path
from .views import CustomAPI


urlpatterns = [
    path("api", CustomAPI.as_view(), name="custom_api"),
]

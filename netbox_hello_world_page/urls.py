from django.urls import path
from .views import HelloWorldView


urlpatterns = [
    # The value in the "name" argument is used in menu item in navigation.py
    path("helloworldpage/", HelloWorldView.as_view(), name="hello_world"),
]

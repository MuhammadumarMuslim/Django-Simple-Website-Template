from django.urls import path
from .views import register, index_page, ios_page, android_page
urlpatterns = [
    path('register/', register, name="register"),
    path('', index_page, name="index_page"),
    path('ios/', ios_page, name="ios"),
    path('android/', android_page, name="android")
]

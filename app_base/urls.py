from django.urls import path

from app_base.views import home

urlpatterns = [
    path('', home, name='home'),
]
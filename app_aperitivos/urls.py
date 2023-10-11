from django.urls import path

from app_aperitivos.views import video, indice

app_name='app_aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
    path('', indice, name='indice'),
]

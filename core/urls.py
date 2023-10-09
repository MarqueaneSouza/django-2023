
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_base.urls')),
    path('app_aperitivos/', include('app_aperitivos.urls')),

]

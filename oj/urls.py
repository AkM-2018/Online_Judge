from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_judge.urls')),
    path('authentication/', include('django.contrib.auth.urls')),
    path('authentication/', include('authentication.urls')),
]

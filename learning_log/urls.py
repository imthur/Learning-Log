from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Define the URL patterns for the admin site
    path('', include('learning_logs.urls')), # Include the URL patterns from the learning_logs app
]


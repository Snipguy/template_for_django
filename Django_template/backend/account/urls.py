from django.urls import path
from .views import register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    # Add login/logout URLs later
]

from django.urls import path
from date.views import *

urlpatterns = [
    path('', index, name='index')
]
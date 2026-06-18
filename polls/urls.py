from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('owner', views.owner, name='owner'),
]

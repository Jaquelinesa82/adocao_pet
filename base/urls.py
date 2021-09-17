from django.urls import path
from base.views import login

app_name = 'base'
urlpatterns = [
    path('', login, name='login'),
]
from django.urls import path
from sos_animal import views
from django.views.generic import RedirectView


app_name = 'sos_animal'
urlpatterns = [
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),
    path('', RedirectView.as_view(url='pet/all/')),
    path('pet/all/', views.list_all_pets),
    path('pet/user/', views.list_user_pet),
]
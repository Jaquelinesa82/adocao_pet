from django.urls import path
from sos_animal import views
from django.views.generic import RedirectView


app_name = 'sos_animal'
urlpatterns = [
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('login/submit', views.submit_login),
    path('', RedirectView.as_view(url='pet/all/')),
    path('pet/all/', views.list_all_pet),
    path('pet/user/', views.list_user_pet),
    path('pet/detail/<slug:id>/', views.pet_detail),
    path('pet/register/', views.register_pet),
    path('pet/register/submit', views.register_submit),
    path('pet/delete/<slug:id>/', views.delete_pet),
]
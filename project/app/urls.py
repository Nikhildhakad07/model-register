from django.urls import path,include
from app import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('first/',views.first,name='first'),
    path('last/',views.last,name='last'),
    path('latest/',views.latest,name='latest'),
    path('earliest/',views.earliest,name='earliest'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.sayhello, name="sayhello"),
    path('hello2/', views.sayhello2, name="sayhello2"),
    path('fuckyou/', views.sayfuckyou, name="sayfuckyou"),
    path('mems/', views.mems, name="mems"),
    path('mems/details/<int:id>', views.details, name='details'),
    path('',views.main,name='main'),
    path('testing/',views.testing,name='testing'),
    path('ifa/',views.ifa,name='ifa'),
    ]
from django.urls import path
from authenticate import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_reg, name='login')
]

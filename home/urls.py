from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='show.login'),
    path('index/', views.index, name='show.index'),
    path('user_create/', views.create_user, name='create.user'),
    path('welcome/', views.welcome, name='show.welcome'),
    path('logout/', views.logout, name='show.logout'),

]

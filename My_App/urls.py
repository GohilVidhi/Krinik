"""
URL configuration for My_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import*
urlpatterns = [
   
    # path('get/', League_view.as_view()),
    # path('get/<int:id>/', League_view.as_view()),
    
    ##------LEAGUE_GET-----------
    path('league_get/', League_view.as_view()),
    path('league_get/<int:id>/', League_view.as_view()),


    ##------TEAM_GET-----------
    path('team_get/', Team_view.as_view()),
    path('team_get/<int:id>/', Team_view.as_view()),
    
    ##------PLAYER_GET-----------
    path('player_get/', Player_view.as_view()),
    path('player_get/<int:id>/', Player_view.as_view()),
    
    
    ##------POOL_GET-----------
    path('pool_get/', pool_view.as_view()),
    path('pool_get/<int:id>/', pool_view.as_view()),
    
    # path('admin/get_players/', get_players, name='get_players'),
    path('pair_get/', Pair_view.as_view()),
    path('pair_get/<int:id>/', Pair_view.as_view()),
    
]

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
    
   ##------PAIR_GET-----------
    path('pair_get/', Pair_view.as_view()),
    path('pair_get/<int:id>/', Pair_view.as_view()),
    
    ##------PAIR_GET_CAPTAIN-----------
    path('pair_captain_get/', Pair_with_captain_view.as_view()),
    path('pair_captain_get/<int:id>/', Pair_with_captain_view.as_view()),
    
    ##------PAIR_GET_CAPTAIN_AND_VICE_CAPTAIN-----------
    path('pair_captain_v_get/', Pair_with_captain_v_captain_view.as_view()),
    path('pair_captain_v_get/<int:id>/', Pair_with_captain_v_captain_view.as_view()),
    
    #=================
    path('new_get/', new_view.as_view()),
    path('new_get/<int:id>/', new_view.as_view()),
    
    
    
    ##------MATCH_GET-----------
    path('match_get/', match_view.as_view()),
    path('match_get/<int:id>/', match_view.as_view()),
    
    
    #--------ADD_POOL GET------------------
    path('add_pool_get/', Add_pool_view.as_view()),
    path('add_pool_get/<int:id>/', Add_pool_view.as_view()),
    
    
     #--------CAPTAIN_ADD_POOL GET------------------
    path('captain_add_pool_get/', Captain_Add_Pool_view.as_view()),
    path('captain_add_pool_get/<int:id>/', Captain_Add_Pool_view.as_view()),
    
    
    
     #--------VICE_CAPTAIN_ADD_POOL GET------------------
    path('vice_captain_add_pool_get/', Vice_Captain_Add_Pool_view.as_view()),
    path('vice_captain_add_pool_get/<int:id>/', Vice_Captain_Add_Pool_view.as_view()),
    
    #--------POOL DECLARE GET------------------
    path('pool_declare/', Pool_Declare_view.as_view()),
    path('pool_declare/<int:id>/', Pool_Declare_view.as_view()),
    
    path('user_get/', user_view.as_view()),
    path('user_get/<int:id>/', user_view.as_view()),

    path('login_get/', login_view.as_view()),
    path('login_get/<int:id>/', login_view.as_view()),
]








##------PAIR_GET  format for  (post/update) -----------

# {"pool_name": "pool2",
#     "player_1": "rohit",
#     "player_2": "virat",
#     "limit": 3}

#===============
# {"pool_name": "pool4",
# "select_match":"ipl11 vs t11   12/06/2024 20:00",
#     "player_1": "rohit",
#     "player_2": "virat",
   
   
#     "limit": 2}

#----------------- PAIR_GET_CAPTAIN_AND_VICE_CAPTAIN------------
# {"pool_name": "dhruvil",
# "select_match":"CSK vs RCB 16-07-2024 12:34",
#     "player_1": "mahendra singh dhoni",
#     "player_2": "virat kohli",
#     "player_3": "ruturaj gaikwad",
   
#     "limit": 23}
#===============================================
# MATCH_GET format for  (post/update) 
# { "select_league":  "abc",
#               "select_team_A":   "ipl",
#             "select_player_A": [ "virat" ],
#             "select_team_B": 
#              "tttt",
#             "select_player_B": ["dhoni"
#                ],
#             "match_start_date": "10/06/2024"
#         }
#-------------------------------------------
# MATCH update runs 

# {
#     "select_league": "abc",
#     "select_team_A": "ipl",
#     "select_player_A": [
#         {
#             "player_name": "virat",
#             "total_run": 55
#         }
#     ],
#     "select_team_B": "tttt",
#     "select_player_B": [
#         {
#             "player_name": "dhoni",
#             "total_run": 44
#         }
#     ],
#     "match_start_date": "10/06/2024"
# }



#==============================================
# ADD_POOL GET  format for   (post/update)
# {
#     "select_match":"ipl vs tttt",
#     "pool_type": "mmm",
#     "pool_name": "pool1",
#     "price": [
#         200,
#         300,
#         500,
#         600
#     ],
#     "winning_price": 2100,
#     "fantacy_start_date": "20/06/2024",
#     "fantacy_end_date": "30/06/2024"
# }



#==============================================
# Pool_Declare  GET  format for   (post/update)

# {
           
#             "player_declare": "dhoni" ,
#             "team_declare":"tttt",
#             "total_run": 202
#         }
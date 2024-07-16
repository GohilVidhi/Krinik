from typing import Any
from django.db import models
from django_mysql.models import ListTextField



# Create your models here.
class League(models.Model):
    league_name=models.CharField(max_length=50,blank=True,null=True)
    short_league_name=models.CharField(max_length=50,blank=True,null=True)
    start_league_date=models.CharField(max_length=50,blank=True,null=True)
    end_league_date=models.CharField(max_length=50,blank=True,null=True)
    league_image=models.ImageField(upload_to="league_image_media")
    
    
    
    
    def __str__(self):
        return self.league_name
    
    
    
    
#------Team Models----------   
    
class Team(models.Model):
    league_name=models.ForeignKey(League,on_delete=models.CASCADE)  
    team_name=models.CharField(max_length=50,blank=True,null=True)      
    team_short_name=models.CharField(max_length=50,blank=True,null=True)      
    team_image=models.ImageField(upload_to="league_image_media")
    team_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.team_name
    
    
    
#------Player Models----------  
   

class Player(models.Model):
    league_name=models.ForeignKey(League,on_delete=models.CASCADE)  
    team_name=models.ForeignKey(Team,on_delete=models.CASCADE)  
    player_name=models.CharField(max_length=50,blank=True,null=True)      
    player_short_name=models.CharField(max_length=50,blank=True,null=True)      
    player_image=models.ImageField(upload_to="league_image_media")
    total_run=models.IntegerField(blank=True,null=True)  


    def __str__(self):
        return self.player_name        
    
    
#------Pool Models----------      
 

class Pool(models.Model):
    pool_type = models.CharField(max_length=50, blank=True, null=True)      
    pool_name = models.CharField(max_length=50, blank=True, null=True)      
    entry_fee = models.IntegerField(blank=True, null=True)
    # Uncomment the following line if you want to associate a pool with a league.
    # league_name = models.ForeignKey(League, on_delete=models.CASCADE)  
    team_name1 = models.ForeignKey(Team, related_name='team1_pools', on_delete=models.CASCADE,blank=True, null=True) 
    player_name1 = models.ManyToManyField(Player, related_name='player1_pools',blank=True, null=True)  
    team_name2 = models.ForeignKey(Team, related_name='team2_pools', on_delete=models.CASCADE,blank=True, null=True) 
    player_name2 = models.ManyToManyField(Player, related_name='player2_pools',blank=True, null=True) 
    start_pool_date=models.CharField(max_length=50,blank=True,null=True)
    end_pool_date=models.CharField(max_length=50,blank=True,null=True)
    
    league_data=models.ForeignKey(League, related_name='league_pools', on_delete=models.CASCADE,blank=True, null=True)
    

    def __str__(self):
        return self.pool_name
    
    
    
# class Pair(models.Model):
#     player_id=models.ForeignKey(Player, on_delete=models.CASCADE)
#     player_1 = models.ForeignKey(Player,on_delete=models.CASCADE) 
#     player_2 = models.ForeignKey(Player,  on_delete=models.CASCADE) 
#     limit=models.IntegerField()
    
#     def __str__(self):
#         return self.player_id
    
    
  

# class Pair(models.Model):

#     pool_name=models.ForeignKey(Pool, on_delete=models.CASCADE,blank=True,null=True)
    
#     player_1=models.ForeignKey(Player, related_name='pool_player1', on_delete=models.CASCADE,blank=True,null=True)
    
#     player_2=models.ForeignKey(Player, related_name='pool_player2', on_delete=models.CASCADE,blank=True,null=True)
#     limit=models.IntegerField()

#     def __str__(self):
#         return str(self.pool_id) 
    
    
    
class new(models.Model):

    widget_group_ids = ListTextField(
            base_field=models.IntegerField(),
            size=100,  # Maximum of 100 ids in list
            blank=True,null=True
        )

    
    
class Match(models.Model):
    select_league=models.ForeignKey(League,on_delete=models.CASCADE,blank=True, null=True) 
    
    select_team_A = models.ForeignKey(Team, related_name='team_A', on_delete=models.CASCADE,blank=True, null=True) 
    select_player_A = models.ManyToManyField(Player, related_name='select_player_A',blank=True, null=True)  
    
    select_team_B = models.ForeignKey(Team, related_name='team_B', on_delete=models.CASCADE,blank=True, null=True) 
    select_player_B = models.ManyToManyField(Player, related_name='select_player_B',blank=True, null=True) 
    
    match_start_date=models.CharField(max_length=50,blank=True,null=True)
    match_end_date=models.CharField(max_length=50,blank=True,null=True)
    match_display_name = models.CharField(max_length=255, blank=True, default='')
    def __str__(self):
        return self.match_display_name
    
    def save(self, *args, **kwargs):
        if not self.match_display_name:
            self.match_display_name = f"{self.select_team_A.team_short_name} vs {self.select_team_B.team_short_name}   {self.match_start_date}"
        super().save(*args, **kwargs)
        
        

class Add_Pool(models.Model):
    select_match=models.ForeignKey(Match,on_delete=models.CASCADE, blank=True, null=True)
    pool_type = models.CharField(max_length=50, blank=True, null=True)      
    pool_name = models.CharField(max_length=50, blank=True, null=True)      
    price = ListTextField(base_field=models.IntegerField(),size=100,blank=True,null=True)
    winning_price=models.IntegerField()
   
    fantacy_start_date=models.CharField(max_length=50,blank=True,null=True)
    fantacy_end_date=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.pool_name
    
    
    
#==============Pair Models=======================
    
class Pair(models.Model):

    pool_name=models.ForeignKey(Add_Pool, on_delete=models.CASCADE,blank=True,null=True)
    select_match=models.ForeignKey(Match,on_delete=models.CASCADE, blank=True, null=True)
    player_1=models.ForeignKey(Player, related_name='pool_player1', on_delete=models.CASCADE,blank=True,null=True)
    
    player_2=models.ForeignKey(Player, related_name='pool_player2', on_delete=models.CASCADE,blank=True,null=True)
    limit=models.IntegerField()

    def __str__(self):
        return str(self.pool_name) 

#=======================Pair_with_captain models===============================
class Pair_with_captain(models.Model):

    pool_name=models.ForeignKey(Add_Pool, on_delete=models.CASCADE,blank=True,null=True)
    select_match=models.ForeignKey(Match,on_delete=models.CASCADE, blank=True, null=True)
    player_1=models.ForeignKey(Player, related_name='pair_with1', on_delete=models.CASCADE,blank=True,null=True)
    
    player_2=models.ForeignKey(Player, related_name='pair_with2', on_delete=models.CASCADE,blank=True,null=True)
    limit=models.IntegerField()

    def __str__(self):
        return str(self.pool_name)     
  

#==========Pair_with_captain_and_vice_captain models=================
class Pair_with_captain_and_v_captain(models.Model):

    pool_name=models.ForeignKey(Add_Pool, on_delete=models.CASCADE,blank=True,null=True)
    select_match=models.ForeignKey(Match,on_delete=models.CASCADE, blank=True, null=True)
    player_1=models.ForeignKey(Player, related_name='pair_with_v1', on_delete=models.CASCADE,blank=True,null=True)
    
    player_2=models.ForeignKey(Player, related_name='pair_with_v2', on_delete=models.CASCADE,blank=True,null=True)
    player_3=models.ForeignKey(Player, related_name='pair_with_v3', on_delete=models.CASCADE,blank=True,null=True)
    limit=models.IntegerField()

    def __str__(self):
        return str(self.pool_name)     
      
    
#================== Captain_Add_Pool Models================= 

class Captain_Add_Pool(models.Model):
    select_league = models.ForeignKey(League, on_delete=models.CASCADE, blank=True, null=True)
    select_team_A = models.ForeignKey(Team, related_name='captain_team_A', on_delete=models.CASCADE, blank=True, null=True)
    select_player_A = models.ManyToManyField(Player, related_name='captain_select_player_A', blank=True)
    select_team_B = models.ForeignKey(Team, related_name='captain_team_B', on_delete=models.CASCADE, blank=True, null=True)
    select_player_B = models.ManyToManyField(Player, related_name='captain_select_player_B', blank=True)
    captain = models.ManyToManyField(Player, related_name='captain_name', blank=True)
   
    match_start_date = models.CharField(max_length=50, blank=True, null=True)
    match_display_name = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.match_display_name
    
    def save(self, *args, **kwargs):
        if not self.match_display_name:
            self.match_display_name = f"{self.select_team_A.team_name} vs {self.select_team_B.team_name}"
        super().save(*args, **kwargs)
        
        
        
        
#================== Vice_Captain_Add_Pool Models=================
        
        

class Vice_Captain_Add_Pool(models.Model):
    select_league = models.ForeignKey(League, on_delete=models.CASCADE, blank=True, null=True)
    select_team_A = models.ForeignKey(Team, related_name='vice_captain_team_A', on_delete=models.CASCADE, blank=True, null=True)
    select_player_A = models.ManyToManyField(Player, related_name='vice_captain_select_player_A', blank=True)
    select_team_B = models.ForeignKey(Team, related_name='vice_captain_team_B', on_delete=models.CASCADE, blank=True, null=True)
    select_player_B = models.ManyToManyField(Player, related_name='vice_captain_select_player_B', blank=True)
    captain = models.ManyToManyField(Player, related_name='main_captain_name', blank=True)
    vice_captain = models.ManyToManyField(Player, related_name='select_vice_captain', blank=True)
    match_start_date = models.CharField(max_length=50, blank=True, null=True)
    match_display_name = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.match_display_name
    
    def save(self, *args, **kwargs):
        if not self.match_display_name:
            self.match_display_name = f"{self.select_team_A.team_name} vs {self.select_team_B.team_name}"
        super().save(*args, **kwargs)
        

#=================POOL DECLARE MODELS========================
class Pool_Declare(models.Model):
    player_declare=models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
    team_declare=models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, null=True)
    total_run=models.IntegerField(blank=True,null=True)
    
    
class user(models.Model):
    name=models.CharField(max_length=100)
    modile_no=models.IntegerField()
    email=models.EmailField(max_length=100)
    date_time=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to="league_image_media")
    wallet_amount=models.IntegerField()
    winning_amount=models.IntegerField()

    def __str__(self):
        return self.name 

class login_user(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.email     
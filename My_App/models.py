from django.db import models

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
    
    
  

class Pair(models.Model):

    pool_id=models.ForeignKey(Pool, on_delete=models.CASCADE,blank=True,null=True)
    
    player_1=models.ForeignKey(Player, related_name='pool_player1', on_delete=models.CASCADE,blank=True,null=True)
    
    player_2=models.ForeignKey(Player, related_name='pool_player2', on_delete=models.CASCADE,blank=True,null=True)
    limit=models.IntegerField()

    def __str__(self):
        return str(self.pool_id) 
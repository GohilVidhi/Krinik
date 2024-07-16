from rest_framework import serializers
from .models import*
from django.db.models import Q


from django.core.exceptions import ObjectDoesNotExist

#-------------League_serializers view----------------

class League_serializers(serializers.Serializer):
    # id=serializers.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    id = serializers.IntegerField(required=False)
    league_name=serializers.CharField(max_length=50,required=True)
    short_league_name=serializers.CharField(max_length=50,required=True)
    start_league_date=serializers.CharField(max_length=50,required=True)
    end_league_date=serializers.CharField(max_length=50,required=True)
    league_image=serializers.ImageField(required=True)

    class Meta:
        models=League
        fields ='__all__'
        exclude = ('id',) 

    def create(self, validated_data):
        return League.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.league_name=validated_data.get('league_name',instance.league_name)
        
        instance.short_league_name=validated_data.get('short_league_name',instance.short_league_name)
        
        instance.start_league_date=validated_data.get('start_league_date',instance.start_league_date)
        instance.end_league_date=validated_data.get('end_league_date',instance.end_league_date)
        
        instance.league_image=validated_data.get('league_image',instance.league_image)

        instance.save()
        return instance        
    
    
    
    
#-------------Team_serializers view----------------
    

    
class Team_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    league_name = serializers.SlugRelatedField(slug_field='league_name', queryset=League.objects.all(), required=True)
    team_name = serializers.CharField(max_length=100, required=True)
    team_short_name=serializers.CharField(max_length=50,required=True)
    team_image=serializers.ImageField(required=True)
    team_date=serializers.DateField(read_only=True,required=False)
    class Meta:
        model = Team
        fields = '__all__'
        exclude = ('id',) 
    
    
    def create(self, validated_data):
        return Team.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.league_name=validated_data.get('league_name',instance.league_name)
        instance.team_name=validated_data.get('team_name',instance.team_name)
        instance.team_short_name=validated_data.get('team_short_name',instance.team_short_name)
        instance.team_image=validated_data.get('team_image',instance.team_image)
        instance.team_date=validated_data.get('team_date',instance.team_date)

        instance.save()
        return instance 
    
    

#-------------Player_serializers view----------------

class Player_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    league_name = serializers.SlugRelatedField(slug_field='league_name', queryset=League.objects.all(), required=True)
    team_name = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.none(), required=True)

    def __init__(self, *args, **kwargs):
        super(Player_serializers, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            data = kwargs['data']
            league_name = data.get('league_name')

            if league_name:
                # Filter team_name queryset based on the league_name provided in the input data
                self.fields['team_name'].queryset = Team.objects.filter(league_name__league_name=league_name)
    
    player_name = serializers.CharField(max_length=100)
    player_short_name=serializers.CharField(max_length=50)
    player_image=serializers.ImageField(required=True)
    total_run=serializers.IntegerField(required=False)
    class Meta:
        model = Player
        fields = '__all__'
        exclude = ('id',) 

     

    def create(self, validated_data):
        return Player.objects.create(**validated_data)



    def update(self, instance, validated_data):
        instance.league_name=validated_data.get('league_name',instance.league_name)
        instance.team_name=validated_data.get('team_name',instance.team_name)
        instance.player_name=validated_data.get('player_name',instance.player_name)
        instance.player_short_name=validated_data.get('player_short_name',instance.player_short_name)
        instance.player_image=validated_data.get('player_image',instance.player_image)
        instance.total_run=validated_data.get('total_run',instance.total_run)
 
        instance.save()
        return instance
    
     
    
#-------------Pool_serializers view---------------- 



class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['player_name','player_image',"player_short_name","total_run"]

class Teamserializers(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_name','team_short_name','team_image']
        
        
class Leagueserializers(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = ['league_name','short_league_name','league_image']
        # fields="__all__"


class PoolSerializer(serializers.ModelSerializer):
    player_name1 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all(), many=True)
    player_name2 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all(), many=True)
    team_name1 = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all())
    team_name2 = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all())
    start_pool_date=serializers.CharField(max_length=50,required=True)
    end_pool_date=serializers.CharField(max_length=50,required=True)
    
    league_data = serializers.SlugRelatedField(slug_field='league_name', queryset=League.objects.all())
    
    class Meta:
        model = Pool
        fields = ['id', 'pool_type', 'pool_name', 'entry_fee','league_data', 'team_name1', 'player_name1', 'team_name2', 'player_name2','start_pool_date','end_pool_date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["player_name1"] = PlayerSerializer(instance.player_name1, many=True).data
        representation["player_name2"] = PlayerSerializer(instance.player_name2, many=True).data
        representation["league_data"] = Leagueserializers(instance.league_data).data
        representation["team_name1"] = Teamserializers(instance.team_name1).data
        representation["team_name2"] = Teamserializers(instance.team_name2).data
        
        return representation

    def update(self, instance, validated_data):
        instance.pool_type = validated_data.get('pool_type', instance.pool_type)
        instance.pool_name = validated_data.get('pool_name', instance.pool_name)
        instance.entry_fee = validated_data.get('entry_fee', instance.entry_fee)
        instance.team_name1 = validated_data.get('team_name1', instance.team_name1)
        instance.team_name2 = validated_data.get('team_name2', instance.team_name2)
        instance.league_data = validated_data.get('league_data', instance.league_data)
        instance.start_pool_date = validated_data.get('start_pool_date', instance.start_pool_date)
        instance.end_pool_date = validated_data.get('end_pool_date', instance.end_pool_date)
        player_name1_data = validated_data.pop('player_name1', [])
        player_name2_data = validated_data.pop('player_name2', [])
        
        

        instance.player_name1.set(
            Player.objects.filter(player_name__in=[player.player_name for player in player_name1_data])
        )
        instance.player_name2.set(
            Player.objects.filter(player_name__in=[player.player_name for player in player_name2_data])
        )
        
        

        instance.save()
        return instance



#===============Pair serializers====================
# pair_1
class AddPool_Serializer(serializers.ModelSerializer):
    class Meta:                                 #show pool data in pair
        model = Add_Pool
        fields = ['id','pool_type', 'pool_name', 'price', 'winning_price', 'fantacy_start_date', 'fantacy_end_date']




class PairSerializer(serializers.ModelSerializer):
    player_1 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all())
    player_2 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all())
    pool_name = serializers.SlugRelatedField(slug_field='pool_name', queryset=Add_Pool.objects.none(), allow_null=True, required=False)
    select_match = serializers.SlugRelatedField(slug_field='match_display_name', queryset=Match.objects.none(), allow_null=True, required=False)
    limit = serializers.IntegerField()
    def __init__(self, *args, **kwargs):
        super(PairSerializer, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            data = kwargs['data']
            league_name = data.get('pool_name')
            match_display_name = data.get('select_match')

            if league_name:
                # Filter pool_name queryset based on the league_name provided in the input data
                self.fields['pool_name'].queryset = Add_Pool.objects.filter(pool_name=league_name,select_match__match_display_name=match_display_name)

            if match_display_name:
                # Filter select_match queryset based on the match_display_name provided in the input data
                self.fields['select_match'].queryset = Match.objects.filter(match_display_name=match_display_name)



    class Meta:
        model = Pair
        fields = ['id', 'pool_name','select_match', 'player_1', 'player_2', 'limit']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["player_1"] = PlayerSerializer(instance.player_1).data
        representation["player_2"] = PlayerSerializer(instance.player_2).data
        representation["pool_name"] = AddPool_Serializer(instance.pool_name).data  #show pool data in pair
       
        representation["select_match"] = Match_Serializer(instance.select_match).data if instance.select_match else None
        return representation


    def create(self, validated_data):
        player_1_name = validated_data.pop('player_1')
        player_2_name = validated_data.pop('player_2')
        limit = validated_data.pop('limit')
        pool_name = validated_data.get('pool_name', None)
        select_match = validated_data.get('select_match', None)

        player_1 = Player.objects.get(player_name=player_1_name)
        player_2 = Player.objects.get(player_name=player_2_name)

        pair = Pair.objects.create(player_1=player_1, player_2=player_2, pool_name=pool_name, limit=limit,select_match=select_match)
        return pair

    def update(self, instance, validated_data):
        player_1_name = validated_data.pop('player_1', None)
        player_2_name = validated_data.pop('player_2', None)
        limit = validated_data.get('limit', instance.limit)
        pool_name = validated_data.get('pool_name', instance.pool_name)


        if player_1_name:
            player_1 = Player.objects.get(player_name=player_1_name)
            instance.player_1 = player_1
        if player_2_name:
            player_2 = Player.objects.get(player_name=player_2_name)
            instance.player_2 = player_2
        instance.select_match = validated_data.get('select_match', instance.select_match)
        instance.limit = limit
        instance.pool_name = pool_name
        instance.save()
        return instance
    
    
 
    
#===============Pair with captain serializers====================
# pair_2
    

class Pair_with_captain_Serializer(serializers.ModelSerializer):
    player_1 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all())
    player_2 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all())
    pool_name = serializers.SlugRelatedField(slug_field='pool_name',queryset=Add_Pool.objects.all(), allow_null=True, required=False)
    select_match = serializers.SlugRelatedField(slug_field='match_display_name', queryset=Match.objects.none(), allow_null=True, required=False)
    limit = serializers.IntegerField()


    def __init__(self, *args, **kwargs):
        super(Pair_with_captain_Serializer, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            data = kwargs['data']
            league_name = data.get('pool_name')
            match_display_name = data.get('select_match')

            if league_name:
                # Filter pool_name queryset based on the league_name provided in the input data
                self.fields['pool_name'].queryset = Add_Pool.objects.filter(pool_name=league_name,select_match__match_display_name=match_display_name)
            
            if match_display_name:
                # Filter select_match queryset based on the match_display_name provided in the input data
                self.fields['select_match'].queryset = Match.objects.filter(match_display_name=match_display_name)
            



    
    class Meta:
        model = Pair_with_captain
        fields = ['id', 'pool_name','select_match' ,'player_1', 'player_2', 'limit']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["player_1"] = PlayerSerializer(instance.player_1).data
        representation["player_2"] = PlayerSerializer(instance.player_2).data
        representation["pool_name"] = instance.pool_name.pool_name if instance.pool_name else None
        representation["select_match"] = Match_Serializer(instance.select_match).data if instance.select_match else None
        return representation

    def create(self, validated_data):
        player_1_name = validated_data.pop('player_1')
        player_2_name = validated_data.pop('player_2')
        limit = validated_data.pop('limit')
        pool_name = validated_data.get('pool_name', None)
        select_match = validated_data.get('select_match', None)

        player_1 = Player.objects.get(player_name=player_1_name)
        player_2 = Player.objects.get(player_name=player_2_name)
        select_match = validated_data.get('select_match', None)

        pair = Pair_with_captain.objects.create(player_1=player_1, player_2=player_2, pool_name=pool_name, limit=limit,select_match=select_match)
        return pair

    def update(self, instance, validated_data):
        player_1_name = validated_data.pop('player_1', None)
        player_2_name = validated_data.pop('player_2', None)
        limit = validated_data.get('limit', instance.limit)
        pool_name = validated_data.get('pool_name', instance.pool_name)

        if player_1_name:
            player_1 = Player.objects.get(player_name=player_1_name)
            instance.player_1 = player_1
        if player_2_name:
            player_2 = Player.objects.get(player_name=player_2_name)
            instance.player_2 = player_2


        instance.select_match = validated_data.get('select_match', instance.select_match)
        instance.limit = limit
        instance.pool_name = pool_name
        instance.save()
        return instance
    
    
#===============Pair with captain and vice captain serializers===============
# pair_3
    

class Pair_with_captain_and_v_captain_Serializer(serializers.ModelSerializer):
    player_1 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all())
    player_2 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all())
    player_3 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all())
    pool_name = serializers.SlugRelatedField(slug_field='pool_name',queryset=Add_Pool.objects.all(), allow_null=True, required=False)
    select_match = serializers.SlugRelatedField(slug_field='match_display_name', queryset=Match.objects.none(), allow_null=True, required=False)
    limit = serializers.IntegerField()


    
    def __init__(self, *args, **kwargs):
        super(Pair_with_captain_and_v_captain_Serializer, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            data = kwargs['data']
            league_name = data.get('pool_name')
            match_display_name = data.get('select_match')

            if league_name:
                # Filter pool_name queryset based on the league_name provided in the input data
                self.fields['pool_name'].queryset = Add_Pool.objects.filter(pool_name=league_name,select_match__match_display_name=match_display_name)
            
            if match_display_name:
                # Filter select_match queryset based on the match_display_name provided in the input data
                self.fields['select_match'].queryset = Match.objects.filter(match_display_name=match_display_name)
            


    class Meta:
        model = Pair_with_captain_and_v_captain
        fields = ['id', 'pool_name','select_match' , 'player_1', 'player_2','player_3', 'limit']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["player_1"] = PlayerSerializer(instance.player_1).data
        representation["player_2"] = PlayerSerializer(instance.player_2).data
        representation["player_3"] = PlayerSerializer(instance.player_3).data
        representation["pool_name"] = instance.pool_name.pool_name if instance.pool_name else None
        representation["select_match"] = Match_Serializer(instance.select_match).data if instance.select_match else None
        return representation

    def create(self, validated_data):
        player_1_name = validated_data.pop('player_1')
        player_2_name = validated_data.pop('player_2')
        player_3_name = validated_data.pop('player_3')
        limit = validated_data.pop('limit')
        select_match = validated_data.get('select_match', None)
        pool_name = validated_data.get('pool_name', None)

        player_1 = Player.objects.get(player_name=player_1_name)
        player_2 = Player.objects.get(player_name=player_2_name)
        player_3 = Player.objects.get(player_name=player_3_name)
        select_match = validated_data.get('select_match', None)

        pair = Pair_with_captain_and_v_captain.objects.create(player_1=player_1, player_2=player_2,player_3=player_3, pool_name=pool_name, limit=limit,select_match=select_match)
        return pair

    def update(self, instance, validated_data):
        player_1_name = validated_data.pop('player_1', None)
        player_2_name = validated_data.pop('player_2', None)
        player_3_name = validated_data.pop('player_3', None)
        limit = validated_data.get('limit', instance.limit)
        pool_name = validated_data.get('pool_name', instance.pool_name)

        if player_1_name:
            player_1 = Player.objects.get(player_name=player_1_name)
            instance.player_1 = player_1
        if player_2_name:
            player_2 = Player.objects.get(player_name=player_2_name)
            instance.player_2 = player_2
        if player_3_name:
            player_3 = Player.objects.get(player_name=player_3_name)
            instance.player_3 = player_3

        
        instance.select_match = validated_data.get('select_match', instance.select_match)
        instance.limit = limit
        instance.pool_name = pool_name
        instance.save()
        return instance
    
    
    
    
#==================================================================

class new_serializers(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    
    widget_group_ids = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=100),
        
        # max_length=2,
    )
    class Meta:
        models = new
        fields ='__all__'
        exclude = ('id',) 

    def create(self, validated_data):
        return new.objects.create(**validated_data)    
    
    def update(self, instance, validated_data):
        instance.widget_group_ids=validated_data.get('widget_group_ids',instance.widget_group_ids)
        instance.save()
        return instance  
    
#=======================Match  Serializer==============
    
class MatchSerializer(serializers.ModelSerializer):
    select_league = serializers.SlugRelatedField(slug_field='league_name', queryset=League.objects.all(), required=False, allow_null=True)
    # select_team_A = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
    
    select_team_A = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.none(), required=True)
 
    
    select_player_A = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all(), many=True, required=False, allow_null=True)
    # select_team_B = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
    
    select_team_B = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.none(), required=True)

    def __init__(self, *args, **kwargs):
        super(MatchSerializer, self).__init__(*args, **kwargs)

        if 'data' in kwargs:
            data = kwargs['data']
            league_name = data.get('select_league')

            if league_name:
                # Filter team_name queryset based on the league_name provided in the input data
                self.fields['select_team_B'].queryset = Team.objects.filter(league_name__league_name=league_name)
                self.fields['select_team_A'].queryset = Team.objects.filter(league_name__league_name=league_name)   
    
    select_player_B = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all(), many=True, required=False, allow_null=True)
    match_start_date = serializers.CharField(max_length=50, required=False, allow_null=True)
    match_end_date = serializers.CharField(max_length=50, required=False, allow_null=True)

    class Meta:
        model = Match
        fields = ['id', 'select_league', 'select_team_A', 'select_player_A', 'select_team_B', 'select_player_B', 'match_start_date','match_end_date','match_display_name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["select_league"] = Leagueserializers(instance.select_league).data
        representation["select_team_A"] = Teamserializers(instance.select_team_A).data
        representation["select_player_A"] = PlayerSerializer(instance.select_player_A, many=True).data
        representation["select_team_B"] = Teamserializers(instance.select_team_B).data
        representation["select_player_B"] = PlayerSerializer(instance.select_player_B, many=True).data
        return representation

    def update(self, instance, validated_data):
        instance.select_league = validated_data.get('select_league', instance.select_league)
        instance.select_team_A = validated_data.get('select_team_A', instance.select_team_A)
        instance.select_team_B = validated_data.get('select_team_B', instance.select_team_B)
        instance.match_start_date = validated_data.get('match_start_date', instance.match_start_date)
        instance.match_end_date = validated_data.get('match_end_date', instance.match_end_date)
        
        select_player_A_data = validated_data.pop('select_player_A', [])
        select_player_B_data = validated_data.pop('select_player_B', [])
        
        instance.select_player_A.set(
            Player.objects.filter(player_name__in=[player.player_name for player in select_player_A_data])
        )
        instance.select_player_B.set(
            Player.objects.filter(player_name__in=[player.player_name for player in select_player_B_data])
        )

        instance.save()
        return instance

#============= Match Serializer for add pool show data===================
class Match_Serializer(serializers.ModelSerializer):
    
    select_team_A = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
    
    select_team_B = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
    select_player_A = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all(), many=True, required=False, allow_null=True)
    select_player_B = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all(), many=True, required=False, allow_null=True)
    class Meta:
        model = Match
        fields = ['select_team_A',"select_player_A",'select_team_B',"select_player_B"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation["select_team_A"] = Teamserializers(instance.select_team_A).data

        representation["select_team_B"] = Teamserializers(instance.select_team_B).data
        
        representation["select_player_A"] = PlayerSerializer(instance.select_player_A, many=True).data
        representation["select_player_B"] = PlayerSerializer(instance.select_player_B, many=True).data
         
        return representation

    def update(self, instance, validated_data):
       
        instance.select_team_A = validated_data.get('select_team_A', instance.select_team_A)
        instance.select_team_B = validated_data.get('select_team_B', instance.select_team_B)


        instance.save()
        return instance
    
    


#=================Add Pool Serializer============================
class AddPoolSerializer(serializers.ModelSerializer):
    select_match = serializers.SlugRelatedField(slug_field='match_display_name', queryset=Match.objects.all(), required=False, allow_null=True)
    price = serializers.ListField(child=serializers.IntegerField(), required=False, allow_null=True)

               
     
    class Meta:
        model = Add_Pool
        fields = ['id', 'select_match', 'pool_type', 'pool_name', 'price', 'winning_price', 'fantacy_start_date', 'fantacy_end_date']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["select_match"] = Match_Serializer(instance.select_match).data if instance.select_match else None
    
        return representation




    def update(self, instance, validated_data):
        instance.select_match = validated_data.get('select_match', instance.select_match)
        instance.pool_type = validated_data.get('pool_type', instance.pool_type)
        instance.pool_name = validated_data.get('pool_name', instance.pool_name)
        instance.price = validated_data.get('price', instance.price)
        instance.winning_price = validated_data.get('winning_price', instance.winning_price)
        instance.fantacy_start_date = validated_data.get('fantacy_start_date', instance.fantacy_start_date)
        instance.fantacy_end_date = validated_data.get('fantacy_end_date', instance.fantacy_end_date)
        
        instance.save()
        return instance
    
    
    
    
    
    
#================Captain Add Pool Serializer=============================
class Captain_Add_PoolSerializer(serializers.ModelSerializer):
    select_league = serializers.SlugRelatedField(slug_field='league_name', queryset=League.objects.all(), required=False, allow_null=True)
    select_team_A = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
    select_team_B = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
    select_player_A = PlayerSerializer(many=True, required=False)
    select_player_B = PlayerSerializer(many=True, required=False)
    captain = PlayerSerializer(many=True, required=False)
    
    match_start_date = serializers.CharField(max_length=50, required=False, allow_null=True)

    class Meta:
        model = Captain_Add_Pool
        fields = ['id', 'select_league', 'select_team_A', 'select_player_A', 'select_team_B', 'select_player_B', 'captain', 'match_start_date', 'match_display_name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.select_league:
            representation["select_league"] = League_serializers(instance.select_league).data
        
        if instance.select_team_A:
            representation["select_team_A"] = Team_serializers(instance.select_team_A).data
        
        if instance.select_team_B:
            representation["select_team_B"] = Team_serializers(instance.select_team_B).data
        
        if instance.select_player_A:
            representation["select_player_A"] = PlayerSerializer(instance.select_player_A.all(), many=True).data
        
        if instance.select_player_B:
            representation["select_player_B"] = PlayerSerializer(instance.select_player_B.all(), many=True).data
        
        if instance.captain:
            representation["captain"] = PlayerSerializer(instance.captain.all(), many=True).data
        
        
        
        return representation

    def update(self, instance, validated_data):
        instance.select_league = validated_data.get('select_league', instance.select_league)
        instance.select_team_A = validated_data.get('select_team_A', instance.select_team_A)
        instance.select_player_A = validated_data.get('select_player_A', instance.select_player_A)
        instance.select_team_B = validated_data.get('select_team_B', instance.select_team_B)
        instance.select_player_B = validated_data.get('select_player_B', instance.select_player_B)
        instance.captain = validated_data.get('captain', instance.captain)
        instance.match_start_date = validated_data.get('match_start_date', instance.match_start_date)
        instance.match_display_name = validated_data.get('match_display_name', instance.match_display_name)
        
        instance.save()
        return instance
    
    


#============================================
# class Captain_Add_PoolSerializer(serializers.ModelSerializer):
#     select_league = serializers.SlugRelatedField(slug_field='league_name', queryset=League.objects.all(), required=False, allow_null=True)
#     select_team_A = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
#     select_team_B = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
#     select_player_A = PlayerSerializer(many=True, required=False)
#     select_player_B = PlayerSerializer(many=True, required=False)
#     captain = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), required=False)
    
#     match_start_date = serializers.CharField(max_length=50, required=False, allow_null=True)

#     class Meta:
#         model = Captain_Add_Pool
#         fields = ['id', 'select_league', 'select_team_A', 'select_player_A', 'select_team_B', 'select_player_B', 'captain', 'match_start_date', 'match_display_name']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
        
#         if instance.select_league:
#             representation["select_league"] = League_serializers(instance.select_league).data
        
#         if instance.select_team_A:
#             representation["select_team_A"] = Team_serializers(instance.select_team_A).data
        
#         if instance.select_team_B:
#             representation["select_team_B"] = Team_serializers(instance.select_team_B).data
        
#         if instance.select_player_A:
#             representation["select_player_A"] = PlayerSerializer(instance.select_player_A.all(), many=True).data
        
#         if instance.select_player_B:
#             representation["select_player_B"] = PlayerSerializer(instance.select_player_B.all(), many=True).data
        
#         if instance.captain:
#             representation["captain"] = PlayerSerializer(instance.captain.all(), many=True).data
        
        
        
#         return representation



#=============Vice Captain Add Pool Serializer===================

class Vice_Captain_Add_PoolSerializer(serializers.ModelSerializer):
    select_league = serializers.SlugRelatedField(slug_field='league_name', queryset=League.objects.all(), required=False, allow_null=True)
    select_team_A = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
    select_team_B = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=False, allow_null=True)
    select_player_A = PlayerSerializer(many=True, required=False)
    select_player_B = PlayerSerializer(many=True, required=False)
    captain = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), required=False, many=True)
    vice_captain = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), required=False, many=True)
    match_start_date = serializers.CharField(max_length=50, required=False, allow_null=True)

    class Meta:
        model = Vice_Captain_Add_Pool
        fields = ['id', 'select_league', 'select_team_A', 'select_player_A', 'select_team_B', 'select_player_B', 'captain', 'vice_captain', 'match_start_date', 'match_display_name']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        if instance.select_league:
            representation["select_league"] = League_serializers(instance.select_league).data
        
        if instance.select_team_A:
            representation["select_team_A"] = Team_serializers(instance.select_team_A).data
        
        if instance.select_team_B:
            representation["select_team_B"] = Team_serializers(instance.select_team_B).data
        
        if instance.select_player_A:
            representation["select_player_A"] = PlayerSerializer(instance.select_player_A.all(), many=True).data
        
        if instance.select_player_B:
            representation["select_player_B"] = PlayerSerializer(instance.select_player_B.all(), many=True).data
        
        if instance.captain:
            representation["captain"] = PlayerSerializer(instance.captain.all(), many=True).data
        
        if instance.vice_captain:
            representation["vice_captain"] = PlayerSerializer(instance.vice_captain.all(), many=True).data
        
        return representation
    
    
    
    
    
    
    def update(self, instance, validated_data):
            instance.select_league = validated_data.get('select_league', instance.select_league)
            instance.select_team_A = validated_data.get('select_team_A', instance.select_team_A)
            instance.select_player_A = validated_data.get('select_player_A', instance.select_player_A)
            instance.select_team_B = validated_data.get('select_team_B', instance.select_team_B)
            instance.select_player_B = validated_data.get('select_player_B', instance.select_player_B)
            instance.captain = validated_data.get('captain', instance.captain)
            instance.vice_captain = validated_data.get('vice_captain', instance.vice_captain)
            instance.match_start_date = validated_data.get('match_start_date', instance.match_start_date)
            instance.match_display_name = validated_data.get('match_display_name', instance.match_display_name)
            
            instance.save()
            return instance
        
    



#==============Pool Declare Serializer=================
class Player_declare_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'player_name','player_short_name','player_image']

class Team_declare_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name','team_short_name','team_image']

class Pool_Declare_Serializer(serializers.ModelSerializer):
    player_declare = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all(), allow_null=True, required=False)
    team_declare = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), allow_null=True, required=False)
    total_run = serializers.IntegerField(required=False, allow_null=True)
    
    class Meta:
        model = Pool_Declare
        fields = ['id', 'player_declare', 'team_declare', 'total_run']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["player_declare"] = Player_declare_Serializer(instance.player_declare).data if instance.player_declare else None
        representation["team_declare"] = Team_declare_Serializer(instance.team_declare).data if instance.team_declare else None
        return representation

    def update(self, instance, validated_data):
        instance.player_declare = validated_data.get('player_declare', instance.player_declare)
        instance.team_declare = validated_data.get('team_declare', instance.team_declare)
        instance.total_run = validated_data.get('total_run', instance.total_run)

        instance.save()
        return instance
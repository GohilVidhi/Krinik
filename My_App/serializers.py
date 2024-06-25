from rest_framework import serializers
from .models import*
from django.db.models import Q


from django.core.exceptions import ObjectDoesNotExist

#-------------League_serializers view----------------

class League_serializers(serializers.Serializer):
    # id=serializers.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    id = serializers.IntegerField(required=False)
    league_name=serializers.CharField(max_length=20,required=True)
    short_league_name=serializers.CharField(max_length=20,required=True)
    start_league_date=serializers.CharField(max_length=20,required=True)
    end_league_date=serializers.CharField(max_length=20,required=True)
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
    team_short_name=serializers.CharField(max_length=20,required=True)
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
    team_name = serializers.SlugRelatedField(slug_field='team_name', queryset=Team.objects.all(), required=True)
    
    player_name = serializers.CharField(max_length=100)
    player_short_name=serializers.CharField(max_length=20)
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
        fields = ['player_name','player_image',"player_short_name"]

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
    start_pool_date=serializers.CharField(max_length=20,required=True)
    end_pool_date=serializers.CharField(max_length=20,required=True)
    
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

class PairSerializer(serializers.ModelSerializer):
    player_1 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all())
    player_2 = serializers.SlugRelatedField(slug_field='player_name', queryset=Player.objects.all())
    pool_name = serializers.SerializerMethodField()
    limit = serializers.IntegerField()

    class Meta:
        model = Pair
        fields = ['id', 'pool_name', 'player_1', 'player_2', 'limit']

    def get_pool_name(self, obj):
        return obj.pool_id.pool_name if obj.pool_id else None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["player_1"] = PlayerSerializer(instance.player_1).data
        representation["player_2"] = PlayerSerializer(instance.player_2).data
        representation["pool_name"] = self.get_pool_name(instance)
        return representation

    def create(self, validated_data):
        player_1_data = validated_data.pop('player_1')
        player_2_data = validated_data.pop('player_2')
        limit = validated_data.pop('limit')
        pool_id = validated_data.get('pool_id', None)

        player_1 = Player.objects.get(player_name=player_1_data)
        player_2 = Player.objects.get(player_name=player_2_data)

        pair = Pair.objects.create(player_1=player_1, player_2=player_2, pool_id=pool_id, limit=limit)
        return pair

    def update(self, instance, validated_data):
        player_1_data = validated_data.pop('player_1', None)
        player_2_data = validated_data.pop('player_2', None)
        limit = validated_data.get('limit', instance.limit)
        pool_id = validated_data.get('pool_id', instance.pool_id)

        if player_1_data:
            player_1 = Player.objects.get(player_name=player_1_data)
            instance.player_1 = player_1
        if player_2_data:
            player_2 = Player.objects.get(player_name=player_2_data)
            instance.player_2 = player_2

        instance.limit = limit
        instance.pool_id = pool_id
        instance.save()
        return instance

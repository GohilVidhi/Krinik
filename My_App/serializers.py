from rest_framework import serializers
from .models import*


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
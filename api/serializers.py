from .models import Artist, Albom, Song
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'




class AlbomSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()

    class Meta:
        model = Albom
        fields = ('id', 'title', 'artist')

class SongSerializer(serializers.ModelSerializer):
    albom = AlbomSerializer()
    class Meta:
        model = Song
        fields = ('id', 'title', 'image', 'albom')





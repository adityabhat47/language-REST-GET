from rest_framework import serializers
from . models import learning

class learningSerializer(serializers.ModelSerializer):

    class Meta:
        model = learning
        fields = ('Language','Rank','Native_speakers_millions','Percentage_of_world_population')
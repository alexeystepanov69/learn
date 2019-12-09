from rest_framework import serializers
from toy.models import Floor


class FloorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Floor
        fields = ['number', 'name', 'has_toilet']
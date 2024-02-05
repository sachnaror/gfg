# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import GeekModel


# Create a model serializer
class GeekSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = GeekModel
        fields = ('title', 'description', 'numb')

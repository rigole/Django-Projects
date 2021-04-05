from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'duration', 'rating']
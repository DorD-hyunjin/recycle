from rest_framework import serializers
from .models import Point
# from django.contrib.auth import authenticate


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['phone_number', 'point']




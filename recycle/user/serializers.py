from rest_framework import serializers
from .models import Point
# from django.contrib.auth import authenticate


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['phone_number', 'point']

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['phone_number', 'recent_point', 'sum_points', 'count', 'recent_date']
#
#
# class RecordSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         record = Record.objects.create(
#             phone_number=validated_data['phone_number'],
#             point=validated_data['point'],
#             sum_points=validated_data['sum_points'],
#             # count=UserSerializer(phone_number).data['count'] + 1
#         )
#
#         return record
#
#     def update(self, validated_data):
#         user = User.objects.create(
#             phone_number=validated_data['phone_number'],
#             recent_point=validated_data['point'],
#             sum_points=validated_data['sum_points'],
#             # count=validated_data['count']
#         )
#
#         return user
#
#     class Meta:
#         model = User, Record
#         fields = ['phone_number', 'recent_point', 'sum_points', 'count', 'recent_date']
#         # model = Record
#         # fields = ['phone_number', 'point', 'sum_points', 'count', 'date']


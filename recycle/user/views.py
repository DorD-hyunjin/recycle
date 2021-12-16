from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Point
from rest_framework.response import Response
from .serializers import PointSerializer
from django.utils import timezone

# Create your views here.


@api_view(['POST'])
def get_points(request):
    """
    전화번호 + 포인트 > 전화번호 + 포인트 + 누적포인트
    """
    serializer = PointSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        user = Point.objects.get(phone_number=serializer.data['phone_number'])
        user.point = user.point + serializer.data['point']
        user.date = timezone.now()
        user.save()
    user = Point.objects.get(phone_number=serializer.data['phone_number'])
    return Response(
        {"phone_number": serializer.data['phone_number'],
         "point": serializer.data['point'],
         "sum_points": user.point})


@api_view(['POST'])
def post_user_info(request):
    """
    전화번호 -> 고객 정보 조회
    """
    pass



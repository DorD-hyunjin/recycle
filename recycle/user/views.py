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
    전화번호, 포인트 저장
    """
    pass

# @api_view(['POST'])
# def get_sum_points(request):
#     """
#     전화번호를 통한 최근의 sum_points 응답 ({"phone_number": "01000000000"} > {"sum_point": "0"})
#     """
#     try:
#         user_phone = User.objects.get(phone_number=request.data['phone_number'])
#         serializer = UserSerializer(user_phone)
#         print(serializer.data)
#         return Response({"sum_point": serializer.data['sum_points']})
#     except User.DoesNotExist:
#         return Response({"sum_point": "0"})
#
#
# @api_view(['POST'])
# def post_user_info(request):
#     """
#     전화번호, 포인트, 누적 포인트 저장 + 추후 카운트 추가
#     """
#     # request - 전화번호, 포인트만(serializer)
#     # recent_date 시스템 날짜
#     record = Record.objects.get()
#         record.is_valid()
#         Record.save()
#
#     serializer = RecordSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "success"})
#     else:
#         return Response({'message': 'error'})


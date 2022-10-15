from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics


from orders import models as orders_models
from ezzy_api import serializers as ezzy_api_serializers


# class OrderList(APIView):
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, format=None):
#         orders = orders_models.Order.objects.all()
#         serializer = ezzy_api_serializers.OrderSerializer(orders, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ezzy_api_serializers.OrderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderList(generics.ListCreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = orders_models.Order.objects.all()
    serializer_class = ezzy_api_serializers.OrderSerializer

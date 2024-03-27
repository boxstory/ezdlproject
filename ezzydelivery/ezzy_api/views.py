import requests
from rest_framework import permissions
from rest_framework import generics
from decouple import config

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


class TookanAPI:
    base_url = "https://api.tookanapp.com/"
    api_key = config("TOOKAN_API_KEY")

    def __init__(self, api_key):
        self.api_key = api_key

    def _make_request(self, endpoint, method="GET", data=None):
        url = self.base_url + endpoint
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        response = requests.request(method, url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_teams(self):
        endpoint = "team/"
        return self._make_request(endpoint)

    def create_task(self, task_data):
        endpoint = "create_task/"
        return self._make_request(endpoint, method="POST", data=task_data)

    def get_task(self, task_id):
        endpoint = f"get_task/{task_id}"
        return self._make_request(endpoint)

    # Add more methods for other API endpoints as needed

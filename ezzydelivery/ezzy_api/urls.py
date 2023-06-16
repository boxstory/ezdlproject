from django.conf.urls import url
from django.urls import path, include
from ezzy_api import views as ezzy_api_views


app_name = 'ezzy_api'
urlpatterns = [
    path('orderlist/', ezzy_api_views.OrderList.as_view(), name='order_list_api'),
    path('task_post/', ezzy_api_views.task_post, name='task_post'),

]

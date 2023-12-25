from django.urls import path
from webpages import views as webpages_views
from delivery import views as delivery_views
from orders import views as orders_views
from product import views as product_views

app_name = 'product'
urlpatterns = [
    # ITEMS
    path('all/',
         product_views.product_list, name='product_list'),
    path('add/',
         product_views.product_add, name='product_add'),
    path('<int:product_id>/delete/',
         product_views.product_delete, name='product_delete'),
    path('<int:product_id>/update/',
         product_views.product_update, name='product_update'),
    # SKUS
    path('skus/all/', product_views.product_sku_list,
         name='product_sku_list'),
    path('add_item_sku/',
         product_views.product_sku_add, name='product_sku_add'),
    path('update_item_sku/<int:sku_id>/',
         product_views.product_sku_update, name='product_sku_update'),
    path('delete_item_sku/<int:sku_id>/',
         product_views.product_sku_delete, name='product_sku_delete'),

     # Product categories
     path('product_categories_list/', product_views.product_categories, name='product_categories'),

     # Product Inventory
     path('product_inventory/', product_views.product_inventory, name='product_inventory'),

]


from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from orders import views as orders_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),




    path('', include('core.urls', namespace='core')),
    path('', include('webpages.urls', namespace='webpages')),

    path('client/', include('client.urls', namespace='client')),
    path('orders/', include('orders.urls', namespace='orders')),

    path('fleet/', include('fleet.urls', namespace='fleet')),
    path('delivery/', include('delivery.urls', namespace='delivery')),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include, re_path

from cars.views import CarAPIList, CarAPIUpdate, CarAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/car/', CarAPIList.as_view()),
    path('api/v1/car/<int:pk>/', CarAPIUpdate.as_view()),
    path('api/v1/car-delete/<int:pk>/', CarAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
]

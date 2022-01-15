from django import urls
from django.urls import path, include
# from .views import ApartmentApiView
from .views import GenericAPIView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('apartment', ApartmentViewSet, basename= 'apartment')

urlpatterns = [
    # path('viewset/', include(router.urls)),
    path('views/', GenericAPIView.as_view()),
    path('views/<int:id>', GenericAPIView.as_view()),
    # path('views/', ApartmentApiView.as_view())
]

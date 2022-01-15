from django import urls
from django.urls import path, include
# from .views import ApartmentApiView
from .views import CreateListAPIView, UpdateDestroyAPIView
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('apartment', ApartmentViewSet, basename= 'apartment')

urlpatterns = [
    # path('viewset/', include(router.urls)),
    path('views/', CreateListAPIView.as_view()),
    path('views/<uuid:pk>', UpdateDestroyAPIView.as_view()),
    # path('views/', ApartmentApiView.as_view())
]

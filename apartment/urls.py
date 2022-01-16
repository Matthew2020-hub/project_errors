from django import urls
from django.urls import path, include
# from .views import ApartmentApiView
from .views import CreateListAPIView, CreateUpdateDestroyAPIView


urlpatterns = [
    path('views/', CreateListAPIView.as_view()),
    path('views/<uuid:apartment_id>', CreateUpdateDestroyAPIView.as_view())
]

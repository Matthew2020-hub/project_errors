from django.http.response import JsonResponse
from django.shortcuts import render
from .serializers import ApartmentSerializer
from .models import Apartment
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated





class CreateListAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permisssion_classes = [IsAuthenticated]

    def get(self, request):
        check = Apartment.objects.all()

        return self.list(check)
        # return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        return self.create(request)




class UpdateDestroyAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
    lookup_field = 'apartment_id'
    authentication_classes = [TokenAuthentication]
    permisssion_classes = [IsAuthenticated]


    def put(self, request, apartment_id):
        query = Apartment.objects.filter(apartment_id=apartment_id)
        if query:
            # serializer = ApartmentSerializer(data=request.data)

            # if serializer.is_valid(raise_exception=True):
            #     query.name = serializer.validated_data['name']
            #     query.category = serializer.validated_data['category']
            #     query.price = serializer.validated_data['price']
            #     query.location = serializer.validated_data['location']
            #     query.agent = serializer.validated_data['agent']

            #     for queue in query:
            #         queue.save()
            return self.update(request)
            
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

    def delete(self, request, apartment_id):
        query = Apartment.objects.get(apartment_id=apartment_id)
        if query:
            # query.delete()
            return self.destroy(request)
    


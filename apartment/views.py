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
    # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permisssion_classes = [IsAuthenticated]


    def put(self, request, pk):
        query = Apartment.objects.filter(apartment_id=pk)
        if query:
            serializer = ApartmentSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                # query.id = serializer.data['apartment_id']
                query.name = serializer.validated_data['name']
                query.category = serializer.validated_data['category']
                query.price = serializer.validated_data['price']
                query.location = serializer.validated_data['location']
                query.agent = serializer.validated_data['agent']

                for queue in query:
                    queue.save()
            return self.update(request)
            
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

    def delete(self, request, pk):
        query = Apartment.objects.filter(apartment_id=pk)
        if query:
            query.delete()
        return self.destroy(request)
    




# class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ApartmentSerializer
#     queryset = Apartment.objects.all()
#     lookup_field = 'id'
#     authentication_classes = [TokenAuthentication]
#     # authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
#     permisssion_classes = [IsAuthenticated]

#     def get2(self, request, id):
#         queryset = Apartment.objects.filter(id = id)
#         article = get_object_or_404(queryset)
#         serializer = ApartmentSerializer(article)
#         return Response(serializer.data)

#     def get(self, request, id):
#         check = Apartment.objects.filter(id=id)
#         if check:
#             return self.list(request)
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     def get1(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

#     def post(self, request, id):
#         return self.create(request)

#     def put(self, request, id):
#         # check = Apartment.objects.filter(id=id)
#         # serializers = ApartmentSerializer(data = request.data, many=True)
#         # if serializers.is_valid():
#         #     serializers.save()
#         # if check:
#         #     cheque = check
#         query = Apartment.objects.filter(id=id)
#         answer = query.id
#         if query:
#             # query = ApartmentSerializer(data=request.data)
#             serializer = ApartmentSerializer(data=request.data)

#             if serializer.is_valid(raise_exception=True):
#                 query.id = request.data['id']
#                 query.name = serializer.validated_data['name']
#                 query.category = serializer.validated_data['category']
#                 query.price = serializer.validated_data['price']
#                 query.location = serializer.validated_data['location']
#                 query.agent = serializer.validated_data['agent']

#                 for queue in query:
#                     queue.save()
#             answer.delete()

#             return self.update(request)
            
#         return Response(status=status.HTTP_401_UNAUTHORIZED)
    

#     def delete(self, request, id):
#         query = Apartment.objects.filter(id=id)
#         if query:
#             query.delete()
#         return self.destroy(request)




# class ApartmentApiView(APIView):
#     # def list(self, request):
#     #     queryset = Apartment.objects.all()
#     #     serializer = ApartmentSerializer(queryset, many=True)
#     #     return Response(serializer.data)

#     def get(self, request, id):
#         try:
#             query = Apartment.objects.get(id=id)
#             serializer = ApartmentSerializer(query)
#             return Response(serializer.data, status = status.HTTP_200_OK)
#         except Apartment.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND)

#     def post(self, request, id):
#         # apart = Apartment.objects.create()
#         serializer = ApartmentSerializer(data = request.data)
#         print(request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # apart = Apartment.objects.create()
#             # print(serializer.data)
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         return Response(status = status.HTTP_400_BAD_REQUEST)

#     def put(self, request, id):
#         query = Apartment.objects.get(id=id)
#         # print(query)
#         if query:
#             # query = ApartmentSerializer(data=request.data)
#             serializer = ApartmentSerializer(data=request.data)

#             if serializer.is_valid(raise_exception=True):
#                 # query.id = request.data['id']
#                 query.name = serializer.validated_data['name']
#                 query.category = serializer.validated_data['category']
#                 query.price = serializer.validated_data['price']
#                 query.location = serializer.validated_data['location']
#                 query.agent = serializer.validated_data['agent']

#                 query.save()
#                 serializer.save()
#                 # query.save(update_fields=['id'])
#                 print(serializer)
#                 # serializer.save()
#                 # query.save()
#                 return Response(serializer.data, status = status.HTTP_201_CREATED)
#             return Response(status = status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         try:
#             query = Apartment.objects.get(id=id)
#             serializer = ApartmentSerializer(query, data=request.data)
#             # serializer.delete()
#             query.delete()
#             return Response(status= status.HTTP_200_OK)
#         except Apartment.DoesNotExist:
#             return Response(status = status.HTTP_403_FORBIDDEN)
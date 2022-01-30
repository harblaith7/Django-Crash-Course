
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from animals_app.models import Animals, Category
from animals_app.serializers import AnimalSerializer, CategorySerializer
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

# Create your views here.

# @api_view()
# def animals_list(request):
#     #### WITHOUT REST FRAMEWORK ##### 

#     animals = Animals.objects.all()

#     return JsonResponse({
#         'animals': list(animals.values())
#     })

#     #################################
#     animals = Animals.objects.all()
#     serializer = AnimalSerializer(animals, many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def create_animal(request):
#     serializer = AnimalSerializer(data=request.data)
#     if(serializer.is_valid()):
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def animal(request, pk):
#     try:
#         animal = Animals.objects.get(pk=pk)
#     except:
#         return Response({'Error': 'Animal does not exists'}, status=HTTP_404_NOT_FOUND)

#     if(request.method == 'GET'):
#         serializer = AnimalSerializer(animal)
#         return Response(serializer.data, status=HTTP_400_BAD_REQUEST)

#     if(request.method == 'PUT'):
#         serializer = AnimalSerializer(animal, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#     if(request.method == 'DELETE'):
#         animal.delete()
#         return Response(status=HTTP_204_NO_CONTENT)


class AnimalList(APIView):

    def get(self, request):
        animals = Animals.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)


class CreateAnimal(APIView):

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AnimalDetail(APIView):

    def get_animal_by_pk(self, pk):
        try:
            return Animals.objects.get(pk=pk)
        except:
            return Response({'Error': 'Animal does not exists'}, status=HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        animal = self.get_animal_by_pk(pk)

        serializer = AnimalSerializer(animal)
        return Response(serializer.data, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        animal = self.get_animal_by_pk(pk)

        serializer = AnimalSerializer(animal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        animal = self.get_animal_by_pk(pk)
        animal.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CreateCategory(APIView):

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class CategoryDetail(APIView):

    def get_category_by_pk(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            return Response({'Error': 'Category does not exists'}, status=HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        category = self.get_category_by_pk(pk)

        serializer = CategorySerializer(category)
        return Response(serializer.data, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        category = self.get_category_by_pk(pk)

        serializer = AnimalSerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_category_by_pk(pk)
        category.delete()
        return Response(status=HTTP_204_NO_CONTENT)

from rest_framework import generics, mixins

class AnimalList2(generics.GenericAPIView):
    queryset = Animals.objects.all()
    serializer_class: AnimalSerializer
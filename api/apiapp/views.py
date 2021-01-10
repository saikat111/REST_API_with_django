from django.shortcuts import render
from rest_framework import viewsets
from .serilizer import categoriesSerilizer
from .models import Categories
from rest_framework.response import Response

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
     queryset = Categories.objects.all()
     serializer_class = categoriesSerilizer


     def retrieve(self, request, *args, **kwargs):
          params = kwargs
          print(params)
          value = Categories.objects.filter(name=params['pk'])
          serializer = categoriesSerilizer(value, many=True, context={'request':request})
          return Response(serializer.data)

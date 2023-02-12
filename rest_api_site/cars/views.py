from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Car
from .serializers import CarSerializer


class CarsAPIView(APIView):
    def get(self, request):
        w = Car.objects.all()
        return Response({'posts': CarSerializer(w, many=True).data})

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Car.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            cat_id=request.data['cat_id']
        )

        return Response({'post': CarSerializer(post_new).data})

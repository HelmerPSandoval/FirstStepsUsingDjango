from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)

# Create your views here.
class HelloWorld(APIView):

    def get(self,request):
        return Response(data="Este es el método get!", status=200)
    def patch(self,request):
        return Response(data="Este es el método patch!", status=200)

    def delete(self,request):
        return Response(data="Este es el método delete!", status=200)

    def post(self,request):
        return Response(data="Este es el método post!", status=200)

class PetListAPIView(ListAPIView):

    def get(self,request):
        return Response(data="Estas son todas mis mascotas!", status=200)

class PetAPIView(RetrieveAPIView):

    def get(self,request):
        return Response(data="Este es el método get de PetAPIView!", status=200)

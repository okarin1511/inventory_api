from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Box
from .serializers import BoxSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsStaff
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BoxDateUsernameFilter, BoxFilter

# Create your views here.

class AllBoxesView(APIView):

    permission_classes=[AllowAny,]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BoxDateUsernameFilter

    def get(self, request):
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)

class CreateBoxesView(APIView):

    permission_classes=[IsAuthenticated, IsStaff]

    def post(self, request):
        serializer = BoxSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateBoxDetails(APIView):

    permission_classes=[IsAuthenticated, IsStaff]

    def get_object(self, id):
        try:
            return Box.objects.get(id=id)

        except Box.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        box = self.get_object(id)
        serializer = BoxSerializer(box)
        return Response(serializer.data)

    def put(self, request, id):
        box = self.get_object(id)
        serializer = BoxSerializer(box, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MyBoxesView(APIView):

    permission_classes=[IsAuthenticated, IsStaff]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BoxFilter

    def get(self, request):
        boxes = Box.objects.filter(createdBy=self.request.user)
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)

class DeleteBox(APIView):  

    permission_classes=[IsAuthenticated, IsStaff]

    def delete(self, request, id):
        box = Box.objects.get(id=id, createdBy=request.user)
        box.delete()
        response = {
            "message": "Success!"
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)





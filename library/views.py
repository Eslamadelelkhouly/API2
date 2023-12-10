from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from django.http import JsonResponse

# Create your views here.
@api_view(['GET','Post'])
def UserList (request):     # for all users
    if request.method == 'GET':
        users = User.objects.all() # queury 
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)
    elif request.method == 'Post':
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED )
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def Userpk(request,pk):
    try:
        user = user.objects.get(pk = pk)
    except user.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT':
        serializer = UserSerializer(user,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.date, status= status.HTTP_200_OK)
        return Response(serializer.date, status= status.HTTP_400_BAD_REQUEST)
    #Delete
    if request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

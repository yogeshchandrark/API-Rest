from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API Views"""
    serializer_class= serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView"""
        an_apiview =[
                'Uses HTTP methods as functions (get, post, patch, put, delete)',
                'Is similer to a traditional Django View',
                'Is mapped manually to URL',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handling partial update"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete and Object"""
        return Response({'method': 'DELETE'})

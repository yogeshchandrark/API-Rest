from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API Views"""

    def get(self, request, format=None):
        """Returns a list of APIView"""
        an_apiview =[
                'Uses HTTP methods as functions (get, post, patch, put, delete)',
                'Is similer to a traditional Django View',
                'Is mapped manually to URL',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})

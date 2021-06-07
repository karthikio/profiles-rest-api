from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):
        new_list = [
            'I\'m Karthik Santhosh',
            'Full Stack Web Developer',
            'Freelancer',
            'Programmer',
        ]

        return Response({'mess': 'Hello World', 'new_list': new_list})

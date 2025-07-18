from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
#read only if the user is not authenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . import permissions
from . import models
from . import serializers

class HelloApiView(APIView):

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        return Response({'mess': 'Hello World'})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, pk=None):
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            'mess','django rest framework',
        ]
        return Response({'message': 'Hello', 'mess': a_viewset})


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serirlizer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        '''handles objects by its id'''
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticatedOrReadOnly,
    )

    # sets the users instance to the data
    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)

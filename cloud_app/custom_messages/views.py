import requests

from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework import status

from .models import Message
from .serializers import MessageSerializer


class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = ()


class GalleryView(views.APIView):
    def get(self, request, format=None):
        # TODO:
        return Response({'detail': 'TODO'})


class JsonPlaceholderView(views.APIView):
    json_placeholder_url = 'https://jsonplaceholder.typicode.com/posts/1/'

    def get(self, request, format=None):
        try:
            response = requests.get(self.json_placeholder_url)
            return Response(response.json())
        except Exception as e:
            return Response(
                {'detai': 'failed to fetch placeholder data: {0}'.format(e)},
                status.HTTP_400_BAD_REQUEST
            )

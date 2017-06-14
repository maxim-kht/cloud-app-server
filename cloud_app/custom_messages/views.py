import boto3
from botocore import session
from botocore.client import Config
import requests

from rest_framework import generics, views, status
from rest_framework.response import Response

from .models import Message
from .serializers import MessageSerializer


class MessageListView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = ()


class GalleryView(views.APIView):
    REGION_NAME = 'ap-south-1'
    BUCKET_NAME = 'gallery-82164'

    def get(self, request, format=None):
        config = Config(signature_version='s3v4', region_name=self.REGION_NAME)

        s3 = boto3.resource('s3', config=config)

        current_session = session.get_session()
        client = current_session.create_client('s3', config=config)

        bucket = s3.Bucket(self.BUCKET_NAME)

        response_data = []

        for obj in bucket.objects.all():
            response_data.append({
                'key': obj.key,
                'url': client.generate_presigned_url(
                    'get_object', Params={'Bucket': bucket.name, 'Key': obj.key}
                )
            })

        return Response(response_data)


class JsonPlaceholderView(views.APIView):
    JSON_PLACEHOLDER_URL = 'https://jsonplaceholder.typicode.com/posts/1/'

    def get(self, request, format=None):
        try:
            response = requests.get(self.JSON_PLACEHOLDER_URL)
            return Response(response.json())
        except Exception as e:
            return Response(
                {'detail': 'failed to fetch placeholder data: {0}'.format(e)},
                status.HTTP_400_BAD_REQUEST
            )

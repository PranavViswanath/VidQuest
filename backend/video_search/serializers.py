from rest_framework import serializers
from .models import Video, VideoFrame

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'file', 'uploaded_at']

class VideoFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoFrame
        fields = ['id', 'video', 'timestamp', 'image']
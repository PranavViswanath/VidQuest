from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class VideoFrame(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='frames')
    timestamp = models.FloatField()
    image = models.ImageField(upload_to='frames/')

    def __str__(self):
        return f"Frame at {self.timestamp:.2f}s of {self.video.title}"
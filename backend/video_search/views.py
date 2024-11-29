import os
import pytube
import speech_recognition as sr
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Video
from .serializers import VideoSerializer
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    @action(detail=False, methods=['post'])
    def upload_youtube_link(self, request):
        url = request.data.get('url')
        if not url:
            return JsonResponse({'error': 'No URL provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Download the video using pytube
            yt = pytube.YouTube(url)
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            if not video_stream:
                return JsonResponse({'error': 'No suitable video stream found'}, status=status.HTTP_400_BAD_REQUEST)

            video_file_path = video_stream.download(output_path='media/videos', filename='downloaded_video.mp4')

            # Extract audio and transcribe it using SpeechRecognition
            recognizer = sr.Recognizer()
            with sr.AudioFile(video_file_path) as source:
                audio = recognizer.record(source)
                transcript = recognizer.recognize_google(audio)

            # Use NLP to process the transcript and answer questions
            answer = self.answer_question(transcript, "What is Python?")  # Example question

            return JsonResponse({'transcript': transcript, 'answer': answer}, status=status.HTTP_200_OK)

        except pytube.exceptions.VideoUnavailable:
            return JsonResponse({'error': 'The requested video is unavailable.'}, status=status.HTTP_404_NOT_FOUND)
        except sr.UnknownValueError:
            return JsonResponse({'error': 'Could not understand audio.'}, status=status.HTTP_400_BAD_REQUEST)
        except sr.RequestError as e:
            return JsonResponse({'error': f'Speech Recognition service error: {e}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def answer_question(self, context, question):
        tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-distilled-squad")
        model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased-distilled-squad")

        inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors='pt')
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']

        with torch.no_grad():
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        
        start_scores = outputs.start_logits
        end_scores = outputs.end_logits

        start_index = torch.argmax(start_scores)
        end_index = torch.argmax(end_scores) + 1

        answer_tokens = input_ids[0][start_index:end_index]
        answer = tokenizer.decode(answer_tokens)

        return answer.strip()
# VidQuest
Talk to your YouTube Video! Paste in video link and ask a natural language question, and get precise answers and timestamps to your query; powered by Django, TypeScript, and PyTorch.


<p align="center"> <img width="592" alt="vidquest splash" src="https://github.com/user-attachments/assets/6f9a4b5e-a109-40c3-9464-6b217e07b6e7"> </p>

## Technical Overview

VideoQuest is a cutting-edge full-stack application that allows users to search and interact with YouTube videos using natural language queries. This project leverages the power of Django for the backend, Next.js for the frontend, and integrates advanced AI technologies for video processing and natural language understanding.

### Technology Stack

#### Backend: Django and Django REST Framework

Django was chosen as the backend framework for its robustness, "batteries-included" approach, and excellent support for building RESTful APIs through Django REST Framework (DRF). Key advantages include:

- Rapid development with built-in admin interface and ORM
- Robust security features out-of-the-box
- Scalability and high performance
- Extensive ecosystem and community support

DRF extends Django's capabilities, providing powerful tools for building Web APIs, including serialization, authentication, and viewsets.

#### Frontend: Next.js

Next.js was selected for the frontend due to its powerful features that enhance React applications:

- Server-Side Rendering (SSR) and Static Site Generation (SSG) for improved performance and SEO
- Automatic code splitting for faster page loads
- API routes for serverless function support
- File-based routing for intuitive project structure
- Built-in CSS support and optimized performance

The combination of Next.js and Django creates a powerful full-stack solution, allowing for a seamless development experience and optimal performance.

### AI and Video Processing

The core of VideoQuest's functionality lies in its AI-powered video processing and natural language understanding capabilities. We utilize Hugging Face's Transformers library for state-of-the-art NLP models.

#### Video Processing Workflow

1. YouTube video download using `pytube`
2. Audio extraction from video
3. Speech-to-text conversion using Google's Speech Recognition API
4. Transcript processing and segmentation

#### Natural Language Processing

We employ a pre-trained question-answering model from Hugging Face (e.g., DistilBERT) to process user queries and find relevant answers within the video transcript. This allows for contextual understanding and precise information retrieval.

### Challenges and Solutions

#### Python Version Compatibility

One significant challenge was aligning the Python version with compatible Hugging Face Transformers. We settled on Python 3.8, which provided a good balance between modern features and library compatibility.

#### Video Processing Optimization

Processing large video files efficiently required careful optimization. We implemented chunked processing and utilized multiprocessing to handle large videos without overwhelming system resources.

#### Frontend-Backend Integration

Ensuring seamless communication between the Next.js frontend and Django backend required careful API design and CORS configuration. We implemented JWT authentication for secure data exchange.

### User Workflow and Experience

The application was designed with the user's journey in mind:

1. User inputs a YouTube URL
2. Backend processes the video and extracts the transcript
3. User enters a natural language query about the video content
4. AI model processes the query and searches the transcript for relevant information
5. Results are displayed with timestamps, allowing users to jump to specific parts of the video

This workflow enables users to quickly find relevant information in long videos without watching them entirely, saving time and enhancing the learning experience.

### Reflections and Future Directions

Building VideoQuest has been an enlightening journey into the world of full-stack development and AI integration. The project demonstrates the power of combining modern web technologies with advanced NLP techniques.

Future enhancements could include:

- Implementing more advanced video analysis techniques (e.g., object detection, sentiment analysis)
- Expanding language support for multilingual video processing
- Integrating with other video platforms beyond YouTube
- Developing a mobile application for on-the-go video searching

VideoQuest showcases the potential of AI in transforming how we interact with video content, opening up new possibilities for education, research, and content discovery.

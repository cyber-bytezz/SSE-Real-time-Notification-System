from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Project, Task, Comment, Notification
from .serializers import ProjectSerializer, TaskSerializer, CommentSerializer
import time
from django.http import StreamingHttpResponse

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

def sse_stream(request):
    def event_stream():
        last_id = 0
        while True:
            notifications = Notification.objects.filter(id__gt=last_id, is_read=False).order_by('id')
            for note in notifications:
                print(f"[SSE] Sending: {note.content}")
                last_id = note.id
                yield f"data: {note.content}\n\n"
            time.sleep(2)
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')

@api_view(['POST'])
def mark_notifications_read(request):
    count = Notification.objects.filter(is_read=False).update(is_read=True)
    return Response({"status": f"{count} notifications marked as read"})

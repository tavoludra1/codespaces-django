
# import viewsets
from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task

# create TaskView class
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    


from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, ToDoSerializer, ColumnSerializer, TaskSerializer
from .models import User, ToDo, Column, Task
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

class ColumnViewSet(ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(methods=['patch'], detail=True)
    def change_task_position(self, request,pk=None):
        if pk is None: 
            return Response({'error': 'An id is required!'}, status=status.HTTP_404_NOT_FOUND) # sem id
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist: # task não encontrada
            return Response({'error':'The given id does not exist'}, status=status.HTTP_404_NOT_FOUND)
        data_position = request.data.get('position')
        if data_position is None:
            return Response({'error': 'Position is required'}, status=status.HTTP_404_NOT_FOUND) # sem o campo position
        try:
            task.position = int(data_position)
        except ValueError:
            return Response({'error': 'Position must be an integer'}, status=status.HTTP_400_BAD_REQUEST) # campo position não é um int
        task.save()
        return Response({'status': 'ok'}, status=status.HTTP_200_OK) # sucesso



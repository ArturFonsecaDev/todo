from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, ToDoSerializer, ColumnSerializer, TaskSerializer, ValidateTaskPositionSerializer
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
    def change_task_position(self, request, pk=None):
        if pk is None:
            return Response({'error': 'An Id is missing!'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Invalid Id'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ValidateTaskPositionSerializer(data=request.data)
        if serializer.is_valid():
            new_position = serializer.validated_data.get('position')
            
            # Obter a coluna atual da tarefa
            current_column = task.column

            # Obter o kanban (ToDo) ao qual a coluna atual pertence
            todo = current_column.todo

            # Buscar a nova coluna com base na posição dentro do ToDo
            try:
                new_column = todo.columns.get(position=new_position)
            except Column.DoesNotExist:
                return Response({'error': 'No column found with the given position!'}, status=status.HTTP_404_NOT_FOUND)

            # Atualizar a coluna da tarefa
            task.column = new_column
            task.save()

            return Response({'success': 'Task moved to new column!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
        




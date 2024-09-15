from rest_framework import serializers
from .models import User, ToDo, Column, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__' 


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = '__all__' 
        read_only_fields = ['position']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__' 

# VALIDATE TASK POSITION FOR API CALL
class ValidateTaskPositionSerializer(serializers.ModelSerializer):
    position = serializers.IntegerField(min_value=1)

    class Meta:
        model = Task
        fields = ['position']


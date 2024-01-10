from rest_framework import serializers
from .models import Teacher

# class HelloWorldSerializer(serializers.Serializer):
#     message = serializers.CharField(max_length=100)

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
from django.shortcuts import render
from rest_framework import generics
from .models import Teacher
from .serializers import TeacherSerializer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from .authentication import KeycloakAuthentication
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import JsonResponse


from django.shortcuts import redirect

def keycloak_login(request):
    return redirect("account/social/login/keycloak/")

@method_decorator(login_required, name='dispatch')
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

@method_decorator(login_required, name='dispatch')
class MyApiView(View):
    def get(self, request, *args, **kwargs):
        data = {'message': 'Hello, this is a simple API response!'}
        return JsonResponse(data)


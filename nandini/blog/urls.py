from django.urls import path
from .views import TeacherListCreateView, TeacherRetrieveUpdateDestroyView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('teachers/',login_required( TeacherListCreateView.as_view()), name='teacher-list-create'),
    path('teachers/<int:pk>/',login_required( TeacherRetrieveUpdateDestroyView.as_view()), name='teacher-detail'),
]
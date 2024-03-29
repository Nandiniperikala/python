"""
URL configuration for personal_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from blog.views import keycloak_login
from blog.views import MyApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
    # path('api/teachers/', login_required(include('blog.urls'))),
    path('accounts/', include('allauth.urls')),
    path('keycloak-login/', keycloak_login, name='keycloak-login'),
    path('api/', MyApiView.as_view(), name='my-api'),
]

"""
URL configuration for CRUDoperation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from base.views import home
from base.views import create_note
from base.views import view_notetype
from base.views import create_noteType

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('create-note/', create_note, name = 'create_note'),
    path('view-notetype/', view_notetype, name = 'view_note_type'),
    path('create-notetype/', create_noteType, name = 'create_note_type'),
]

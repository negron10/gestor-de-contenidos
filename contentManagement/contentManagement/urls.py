"""contentManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from hola.views import hola
from hola.chao import chao, principal
from rest_framework.documentation import include_docs_urls
from contentManagement import views

API_TITLE = 'API contentManagement'
API_DESCRIPTION = 'Documentacion API'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', hola),
    url(r'^chao$', chao),
    url(r'^raiz$', principal),
    #url(r'^$', views.index, name='index'),
    url(r'^api/', include(('api.urls', 'api'), namespace='api')),
    url(r'^docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION))
]

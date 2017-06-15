
from django.conf.urls import url, include
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^criar_projeto/$', criar_projeto, name="criar_projeto"),
    url(r'^adiciona_colaboradores/$', adiciona_colaboradores, name="adiciona_colaboradores"),
]
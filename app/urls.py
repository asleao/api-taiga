
from django.conf.urls import url, include
from django.contrib import admin
from app.views import *

urlpatterns = [
    url(r'^criar_projeto/$', criar_projeto, name="criar_projeto"),
    url(r'^adicionar_colaboradores/$', adicionar_colaboradores, name="adicionar_colaboradores"),
    url(r'^remover_colaboradores/$', remover_colaboradores, name="remover_colaboradores"),
]
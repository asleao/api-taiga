from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from taiga import TaigaAPI
import requests
import json


def get_token(username,password):
	api = TaigaAPI()
	api.auth(
	    username=username,
	    password=password
	)
	print (api.token)

def criar_projeto(request):
	api = TaigaAPI(token= request.POST['token'])
	projeto = api.projects.create(request.POST['nome_projeto'], request.POST['descricao_projeto'], is_private = False)

def adiciona_colaboradores():
 	api = TaigaAPI()
 	colaboradores = ['asleao']
 	api.auth(
	    username='lesw',
	    password='les123'
	)

 	url = 'https://api.taiga.io/api/v1/memberships'
 	data_json ={"project": 1, "role": 3, "username": "test-user@test.com"}	
 	# authorization = 'Bearer '+ api.token 	
	headers = {'Content-Type': 'application/json', 'Authorization':'Bearer <token>'}

	r = requests.post(url, data=json.dumps(data_json), headers=headers)

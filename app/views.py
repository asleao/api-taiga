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
	api = TaigaAPI(token=request.POST['token'])
	usernames = request.POST['usernames']
	projeto_nome = request.POST['nome_projeto']

	projeto = api.projects.get_by_slug(projeto_nome)	
	role = projeto.add_role('Desenvolvedor', permissions=["add_issue", "modify_issue"])
	for username in usernames:			
		url = 'https://api.taiga.io/api/v1/memberships'
		data_json ={"project": projeto.id, "role": role.id, "username": username}	
		authorization = 'Bearer '+ api.token 	
		headers = {'Content-Type': 'application/json', 'Authorization': authorization}

		r = requests.post(url, data=json.dumps(data_json), headers=headers)
		print(r.content)

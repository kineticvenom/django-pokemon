from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests as HTTP_Client
import random

# Create your views here.

def pokemon_team(request):
    team_list = []
    random_starter = random.randrange(1,898)
        
    endpoint = f"https://pokeapi.co/api/v2/pokemon/{random_starter}"
    API_response = HTTP_Client.get(endpoint)
    responseJSON = API_response.json()

    team_type = responseJSON['types'][0]['type']['name']
    starter = responseJSON['sprites']['front_default']

    team_list.append(starter)

    while len(team_list) < 6:
        random_pokemon = random.randrange(1,898)
        end = f"https://pokeapi.co/api/v2/pokemon/{random_pokemon}"
        API_response = HTTP_Client.get(end)
        responseJSON = API_response.json()
        pokemon = responseJSON['sprites']['front_default']
        pokemon_type = responseJSON['types'][0]['type']['name']

        if pokemon_type == team_type and pokemon not in team_list :
            team_list.append(pokemon)

    response = render(request, 'pokemon_app/index.html', {'team_list': team_list})

    return response
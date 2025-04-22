
import requests
from django.shortcuts import render

def champion_list(request):
    url = "http://ddragon.leagueoflegends.com/cdn/13.24.1/data/es_ES/champion.json"
    response = requests.get(url)
    champions = []

    if response.status_code == 200:
        data = response.json()
        champions = [
            {
                'id': champ_data['id'],
                'name': champ_data['name'],
                'title': champ_data['title'],
                'image': f"http://ddragon.leagueoflegends.com/cdn/13.24.1/img/champion/{champ_data['id']}.png"
            }
            for champ_data in data['data'].values()
        ]
    
    return render(request, 'lol/champion_list.html', {'champions': champions})

def champion_detail(request, champion_id):
    url = f"http://ddragon.leagueoflegends.com/cdn/13.24.1/data/es_ES/champion/{champion_id}.json"
    response = requests.get(url)
    champion = None

    if response.status_code == 200:
        data = response.json()
        champion_data = data['data'][champion_id]
        champion = {
            'id': champion_data['id'],
            'name': champion_data['name'],
            'title': champion_data['title'],
            'lore': champion_data['lore'],
            'image': f"http://ddragon.leagueoflegends.com/cdn/13.24.1/img/champion/{champion_id}.png",
            'spells': champion_data['spells'],
            'stats': {
                'Vida': champion_data['stats']['hp'],
                'Regeneración de vida': champion_data['stats']['hpregen'],
                'Maná': champion_data['stats']['mp'],
                'Regeneración de maná': champion_data['stats']['mpregen'],
                'Velocidad de movimiento': champion_data['stats']['movespeed'],
                'Armadura': champion_data['stats']['armor'],
                'Resistencia mágica': champion_data['stats']['spellblock'],
                'Rango de ataque': champion_data['stats']['attackrange'],
                'Daño de ataque': champion_data['stats']['attackdamage'],
                'Velocidad de ataque': champion_data['stats']['attackspeed'],
                'Crítico': champion_data['stats']['crit']
            }
        }

    return render(request, 'lol/champion_detail.html', {'champion': champion})

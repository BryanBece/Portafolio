# pokemon/views.py
import requests
from django.http import JsonResponse
from django.shortcuts import render

# Diccionario de traducción
TRANSLATIONS = {
    "normal": "Normal",
    "fire": "Fuego",
    "water": "Agua",
    "electric": "Eléctrico",
    "grass": "Planta",
    "ice": "Hielo",
    "fighting": "Lucha",
    "poison": "Veneno",
    "ground": "Tierra",
    "flying": "Volador",
    "psychic": "Psíquico",
    "bug": "Bicho",
    "rock": "Roca",
    "ghost": "Fantasma",
    "dragon": "Dragón",
    "dark": "Siniestro",
    "steel": "Acero",
    "fairy": "Hada",
    "double_damage_to": "Fuerte contra",
    "double_damage_from": "Débil contra",
}

def translate(text):
    """Función para traducir usando el diccionario TRANSLATIONS."""
    return TRANSLATIONS.get(text, text)

def pokemon_list(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=10000"
    response = requests.get(url)
    pokemon_list = []

    if response.status_code == 200:
        data = response.json()
        pokemon_list = [{'name': pokemon['name'], 'url': pokemon['url']} for pokemon in data['results']]
    
    return render(request, 'pokemon/pokemon_list.html', {'pokemon_list': pokemon_list})

def pokemon_detail(request, name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        types = [translate(t['type']['name']) for t in pokemon_data['types']]
        
        # Obtenemos las fortalezas y debilidades del primer tipo
        primary_type = pokemon_data['types'][0]['type']['name']
        type_data_response = requests.get(f"https://pokeapi.co/api/v2/type/{primary_type}")
        
        if type_data_response.status_code == 200:
            type_data = type_data_response.json()
            strong_against = [translate(d['name']) for d in type_data['damage_relations']['double_damage_to']]
            weak_against = [translate(d['name']) for d in type_data['damage_relations']['double_damage_from']]
        else:
            strong_against = []
            weak_against = []
        
        # Obtener la generación
        species_url = pokemon_data['species']['url']
        species_response = requests.get(species_url)
        generation = "Desconocido"
        if species_response.status_code == 200:
            species_data = species_response.json()
            generation = species_data['generation']['name'].replace("generation-", "").capitalize()

        # Obtener estadísticas
        stat_translation = {
            'hp': 'PS',
            'attack': 'Ataque',
            'defense': 'Defensa',
            'special-attack': 'Ataque Especial',
            'special-defense': 'Defensa Especial',
            'speed': 'Velocidad'
        }
        stats = {stat_translation[stat['stat']['name']]: stat['base_stat'] for stat in pokemon_data['stats']}

        
        return JsonResponse({
            'name': pokemon_data['name'],
            'types': types,
            'strong_against': strong_against,
            'weak_against': weak_against,
            'sprite': pokemon_data['sprites']['front_default'],
            'generation': generation,
            'stats': stats,  # Añadir estadísticas aquí
        })
    
    return JsonResponse({'error': 'Pokémon no encontrado'}, status=404)


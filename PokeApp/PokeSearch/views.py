from django.shortcuts import render,redirect
import requests
from PokeSearch import models
# Create your views here.

def PokeSearch(request):
    try:
        dict = {}
        if request.method == "POST" and request.POST.get('Inputvalue'):
            value = request.POST.get('Inputvalue')
            print(f"The Pokémon to search is: {value}")
            dict["PokemonSearch"]=SearchPokemon(value)
            print(dict["PokemonSearch"])
        elif request.method == "POST" and request.POST.get('Savebtn'):
            print(f"{request.POST.get('Savebtn')}...{Pokemon.name}")
            AddPokemon()
        else: 
            print(f"None...")
        
        return render(request,'PokeSearch/pokesearch.html', context=dict)

    except Exception as e:
        print(e)

def PokeView(request):
    try:
        dict = {}
        dict["Pokemons"] = GetSavedPokemon()
        print(dict["Pokemons"])
        return render(request,'PokeSearch/pokeview.html',context=dict)
    except Exception as e:
        print(e)


def GetSavedPokemon():
    try:
        dict = {}
        pokemons = models.Pokemon.objects.all()
        index = 0
        for pokemon in pokemons:
            dict[index] = {"Name":pokemon.name,"Order":pokemon.order,
                    "HP":pokemon.hp,"Attack":pokemon.atk,
                    "SpAttack":pokemon.spatk,"Defense":pokemon.defense,
                    "SpDefense":pokemon.spdef,"Speed":pokemon.speed}
            index = index+1
        return dict
    except Exception as e:
        print(e)

class Pokemon():
    def __init__(self, name,order,hp,atk,spatk,defe,spdef,speed):
        self.name = name
        self.order = order
        self.hp = hp
        self.atk = atk
        self.spatk = spatk
        self.defe = defe
        self.spdef = spdef
        self.speed = speed
    
    def __str__(self):
        return f"name: {self.name}, order: {self.order}, HP: {self.hp}, Attack: {self.atk}, Sp.Atk: {self.spatk}, Defense: {self.defense}, Sp.Def: {self.spdefense}, Speed: {self.speed}"   


def AddPokemon():
    try:
        models.Pokemon.objects.create(order=Pokemon.order,name=Pokemon.name,
                                hp=Pokemon.hp,atk=Pokemon.atk,spatk=Pokemon.spatk,
                                defense=Pokemon.defe,spdef=Pokemon.spdef,
                                speed=Pokemon.speed)
    except Exception as e:
        print(e)


def SearchPokemon(value):
    try:
        dict = {}
        apiurl = f"https://pokeapi.co/api/v2/pokemon/{value}"
        response = requests.get(apiurl)
        if response.status_code == 200:
            data = response.json()
            pokemon = NewPokemon(data)
            dict = {"Name":pokemon.name,"Order":pokemon.order,
                    "HP":pokemon.hp,"Attack":pokemon.atk,
                    "Sp.Attack":pokemon.spatk,"Defense":pokemon.defe,
                    "Sp.Defense":pokemon.spdef,"Speed":pokemon.speed}
            return dict
        elif response.status_code == 404: 
            print("Not found.")
        else:
            print("Unknown error.")
    except Exception as e:
        print(e)


def NewPokemon(data):
        pokemon = Pokemon
        pokemon.name = data["name"]
        pokemon.order = data["order"]
        pokemon.hp = data["stats"][0]["base_stat"]
        pokemon.atk = data["stats"][1]["base_stat"]
        pokemon.spatk = data["stats"][2]["base_stat"]
        pokemon.defe = data["stats"][3]["base_stat"]
        pokemon.spdef = data["stats"][4]["base_stat"]
        pokemon.speed = data["stats"][5]["base_stat"]
        print(pokemon)
        return pokemon

from django.shortcuts import render
import requests
# Create your views here.

def PokeSearch(request):
    try:
        dict = {}
        if request.method == "POST":
            value = request.POST.get("Inputvalue")
            print(f"The Pokémon to search is: {value}")
            dict["Pokemon"]=SearchPokemon(value)
            print(dict["Pokemon"])
        return render(request,'PokeSearch/pokesearch.html', context=dict)

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

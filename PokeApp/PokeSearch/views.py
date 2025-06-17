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


def SearchPokemon(value):
    try:
        dict = {}
        apiurl = f"https://pokeapi.co/api/v2/pokemon/{value}"
        response = requests.get(apiurl)
        if response.status_code == 200:
            data = response.json()
            name = data["name"]
            order = data["order"]
            hp = data["stats"][0]["base_stat"]
            atk = data["stats"][1]["base_stat"]
            spatk = data["stats"][2]["base_stat"]
            defense = data["stats"][3]["base_stat"]
            spdefense = data["stats"][4]["base_stat"]
            speed = data["stats"][5]["base_stat"]
            print(f"name: {name}, order: {order}, HP: {hp}, Attack: {atk}, Sp.Atk: {spatk}, Defense: {defense}, Sp.Def: {spdefense}, Speed: {speed}")
            dict = {"Name":name,"Order":order,"HP":hp,
                    "Attack":atk,"Sp.Attack":spatk,"Defense":defense,
                    "Sp.Defense":spdefense,"Speed":speed}
            return dict
        elif response.status_code == 404: 
            print("Not found.")
        else:
            print("Unknown error.")
    except Exception as e:
        print(e)



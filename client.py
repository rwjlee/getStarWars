import json, requests
from pprint import pprint

API_BASE = 'https://swapi.co/api/'


def get_url(url):
    resp = requests.get(url)
    return json.loads(resp.text)

def get_json(group, id):
    url=API_BASE+group+'/'+str(id)+'/'
    return get_url(url)

def get_person(id):
    return get_json('people', id)

def get_homeworld(id):
    return get_json('planets', id)

def get_film(id):
    return get_json('films', id)

def get_species(id):
    return get_json('species', id)

def get_vehicle(id):
    return get_json('vehicles', id)

def get_starship(id):
    return get_json('starships', id)

def person_fly_vehicle(id):
    person=get_person(id)
    print(person['name'])
    print('vehicles:')
    for url in get_person(id)['vehicles']:
        print('\t'+get_url(url)['name'])

    print('starships:')
    for url in get_person(id)['starships']:
        print('\t'+get_url(url)['name'])

    print("------\n")

def planet_person_vehicle(id):
    planet=get_homeworld(id)
    print(planet['name'])

    for url in planet['residents']:
        person_fly_vehicle(parse_id(url))

    print("================\n")

def parse_id(url):
    if url[-3]=='/':
        return url[-2]
    else:
        return int(url[-3:-1])

def all_planet_person_vehicle():
    id=1

    while id:
        print("planet id: {}".format(id))
        planet_person_vehicle(id)
        if get_homeworld(id)['detail']=="Not found":
            return 0
        else:
            id=id+1


def get_starship_id(name):
    for i in range(2, 37):
        starship=get_starship(i)

        if starship.get('name'):
            print(starship['name'])
            if starship['name']==name:
                return i

    return None

def starship_rider(name):

    starship=get_starship(get_starship_id(name))
    print(starship['name'])
    print("pilots:")
    for url in starship['pilots']:
        person=get_person(parse_id(url))
        print("{} {}".format("\t", person['name']))

def get_planet_residents(planetName):
    for index in range(1, 7):
        home_dict=get_url("https://swapi.co/api/planets/?page="+str(index))
        for value in home_dict['results']:
            if value['name']==planetName:
                return value['residents']

    return []

def get_starship_riders(shipName):
    for index in range(1, 5):
        starship_dict=get_url("https://swapi.co/api/starships/?page="+str(index))
        for value in starship_dict['results']:
            if value['name']==shipName:
                return value['pilots']

    return []

def resident_on_planet_who_can_ride_vehicle(planetName, shipName):
    #pilots=get_starship_riders(shipName)
    #residents=get_planet_residents(planetName)

    print(pilots)
    print(residents)

    commonList=set()

    for r in residents:
        for p in pilots:
            if r==p:
                commonList.add(r)

    for url in commonList:
        print(get_url(url)["name"])

def get_species_on_planet(planetName):
    residents=get_planet_residents(planetName)
    speciesList=set([])
    for url in residents:
        species=get_url(url)["species"]
        speciesList.add(species[0])

    for sp in speciesList:
        print(get_url(sp)["name"])

    return speciesList

get_species_on_planet("Tatooine")
import json
from pycountry import countries
from pygal_maps_world import maps
#Load data
filename = 'population_data.json'
with open(filename) as file:
    population_data = json.load(file)

# world_population = {}
wmap = maps.World()
wmap.title = "World Population"
world_population = {}
for pop_dict in population_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        try:
            country = countries.get(name=country_name).alpha_2
        except AttributeError as e:
            continue
        
        population = int(float(pop_dict['Value']))
        print(f'{country}: {population:,}')
        world_population[country.lower()] = population


wmap.add("2010", world_population)
wmap.render_to_file("world_population.svg")
# print(world_population)
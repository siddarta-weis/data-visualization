from pygal_maps_world import maps

wm = maps.World()
wm.title = 'North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.add("Teste", {'br': 202000000})

wm.render_to_file('na_america.svg')
# Crea un diccionario llamado planet con los datos propuestos

planet = {
    'name': 'Mars',
    'moons': 2
}
# Muestra el nombre del planeta y el número de lunas que tiene.

print(f'{planet["name"]} has {planet["moons"]} moons')
# Muestra el nombre del planeta y el número de lunas que tiene.

print(f'{planet["name"]} has {planet["moons"]} moons')
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}


# Imprime el nombre del planeta con su circunferencia polar.

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

# Añade el código para determinar el número de lunas.

# Obtenemos la lista de las lunas
# Almacenamos los resultados en una variable moons
moons = planets_moons.values()

# Obtenemos el total de planetas
# Almacenamos los resultados en una variable llamada years
planets = len(planet.moons.keys())



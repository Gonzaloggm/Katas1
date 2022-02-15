#kata 6: Listas ordenadas.

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
print ("Existen ",len(planets),"planetas en nuestro sistema solar")
nplaneta=input("Inserte el nombre del nuevo planeta: ")
planets.append(nplaneta)
print("Ahora tenemos",len(planets),"planetas,el último ingresado fue", planets[-1])

nuevoplaneta=input("Ingrese el nombre del planeta a buscar (primera letra en Mayuscula: )")
planets_index=planets.index(nuevoplaneta)
print ("El numero del planeta buscado es: ",planets_index)

print('Los planetas mas cercanos al sol de ' + nuevoplaneta)
print(planets[0:planets_index])

print('Los planetas mas lejanos al sol de ' + nuevoplaneta)
print(planets[planets_index+1:])

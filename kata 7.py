new_planet=input("Ingrese el nombre del planeta: ")
planets=[]

while new_planet !="Done":
  
        planets.append(new_planet)
        new_planet = input("Introduce el nombre de otro planeta, cuando termines teclea Done:")

print("Usted ingreso",len(planets),"planetas con los nombres:")
for planet in planets:
    print(planet)

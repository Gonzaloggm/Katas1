
print("Operadores Lógicos")

velocidad=input("Inserte la velocidad: ")
masa=input("Inserte el tamaño: ")

# Operadores Lógicos:

# if, operador para saber si se esta cumpliendo una condicion.


if int(velocidad) >19:
         print ("Busca en el cielo la linea blanca del asteroide ")

if int(velocidad) >25:
         print ("Viene a más de 25 km/h ")

elif int(velocidad) <20 and int(masa)<1001:
        print ("No se han detectado Asteroides  peligrosos")

if (int(masa)>25 and int(masa)<1000 and int(velocidad) >25) or int(masa) >1000:   
 print ("Advertencia, el asteroide es peligroso!")

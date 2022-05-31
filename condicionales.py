# Decalramos una variable
from traceback import print_tb


calificacion = input("introduce tu calificacion de la AZ-900")

calificacion = int(calificacion)

# Preguntamos si la calificacion es menor a 700
if calificacion < 700 : 
    print("Ves, por no estudiar") # Si es menor a 700, muestra esto

elif calificacion > 1000:
    print("Mientes")

else: # Si no se cumple el if anterior, pasa a esta linea
    print("Felicidades") # Se ejecuta si ninguno de los if se cumple

# Verificador de mayoria de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Bienvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te fiamos")
elif edad < 0 :
    print("Nique fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")
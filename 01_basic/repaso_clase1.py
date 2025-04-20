#Limpiar pantalla
#Importar libreria os
import os
os.system('cls' if os.name == 'nt' else 'clear')

#Imprimir en pantalla
print(20)
print(type(20))
print(type(20.0))
print(type("20"))
print(type(None))

#casting de tipos
print(int(20.0)) #convierte a entero
print(float(20)) #convierte a flotante
print(str(20)) #convierte a cadena de texto
print(bool(20)) #convierte a booleano. Si es diferente de 0 es True, si es 0 es False
print(bool(0)) #convierte a booleano y devuelve False. Solo el 0 devuelve False
print(bool(-1)) #convierte a booleano y devuelve True
print(bool("")) #convierte a booleano y devuelve False. Cadena de texto vacia es False

print("esto convierte el numero 20 a cadena de texto: " + str(20))
print("La suma de " + str(20) + " + " + str(30) + " es: " + str(20+30))

#variables
name="Eduardo"
print("Mi nombre es: " + name)
name=37 #cambio de tipo de variable mediante reasignacion
anonacimiento=1982
my_name="Eduardo"
print("Mi edad es: " + str(name)) #tipado fuerte. No se puede concatenar cadena de texto con entero. No transforma automaticamente
print(f"Mi edad es: {name} y mi año de nacicimiento es {anonacimiento}") #f-string. Forma mas facil de concatenar
print("............................................")
print(f"Hola {my_name}, tengo {name + 5} años y naci en {anonacimiento}")

nombre = input("Cual es tu nombre? \n")
print(f"Hola {nombre}") #input siempre devuelve una cadena de texto
coutry, city = input("Cual es tu pais y ciudad? \n").split(",") #split separa los valores por coma
print(f"Tu pais es {coutry} y tu ciudad es {city}")
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

import os
os.system("cls")
print("Repaso de listas")

lista = ["uno", 2, 3.14, True]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])

print("-imprimir solo estas posiciones-")
print(lista[0:1]) #el ultimo no se toma en cuenta
print(lista[0:2])

print(lista[:3]) #imprime desde el inicio hasta la posición 3, sin incluirla

listac = [[1,2], ["a", "b"]]
print(listac[0][0])
print(listac[0][1])
print(listac[1][0])
print(listac[1][1])

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("-imprimir indicado el paso-")
print(lista2[::-1])

print("-aquí va el for-")
for i in lista2:
    print(i)

print("prueba rango raro")
print(lista2[1:-1])

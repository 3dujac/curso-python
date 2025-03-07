import os
os.system('cls' if os.name == 'nt' else 'clear')

num = float(input("Introduce tu edad: "))
    
if num < 18:
    print(f"Eres menor de edad 👶 y el valor booleano de {num} es {bool(num)}")
elif num > 18:
    print(f"Eres mayor de edad 🙆‍♂️ y el valor booleano de {num} es {bool(num)}")
else:
    print(f"Felicidades!! 👌 El valor booleano de {num} es {bool(num)}")
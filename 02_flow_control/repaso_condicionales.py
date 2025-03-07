import os
os.system('cls' if os.name == 'nt' else 'clear')

num = float(input("Introduce tu edad: "))
    
if num < 18:
    print("Eres menos de edad 👶 ➖")
elif num > 18:
    print("Eres mayor de edad 🙆‍♂️")
else:
    print("Felicidades!! 👌")
   
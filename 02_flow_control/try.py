try:
    num = float(input("Introduce un número: "))
    
    if num < 0:
        print("El número es negativo")
    elif num > 0:
        print("El número es positivo")
    elif num == 0:
        print("El número es cero")
   
except ValueError:
        print("Eres un puto melon y ni siquiera has introducido un número")
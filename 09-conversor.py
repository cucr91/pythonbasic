temperatura = float(input("Ingresa tu temperatura: "))
escala = input("ingresa tu escala: (F) para Farenheit y (C) para Celsius ").lower()
if escala ==  "f":
    celsius = (temperatura - 32) * 5/9
elif escala ==  ("c"):
    farenheit = (temperatura * 1.8) + 32
    print(farenheit)
else:
    print("Vuelve a ingresar, escala incorrecta ")


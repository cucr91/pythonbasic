puntaje = input("Ingresa tu puntaje:")
#print(type(puntaje))
numero = int(puntaje)


if numero >= 95:
    print("Aprobado con honores")
elif numero >= 50:
    print("Alumno aprobado")
else:
    print("Alumno reprobado")

#print("Fuera del if")

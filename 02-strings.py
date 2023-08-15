texto = "Hola Mundo"
#metodo  funcion incluida dentro de un objeto 
print(texto.upper())
print(texto.lower())
print(texto.find("Mun"))
print(texto.find("mun"))
nuevoTexto = texto.replace("Mundo", "chanchito feliz")
print(texto, nuevoTexto)
print("Mundo" in texto)
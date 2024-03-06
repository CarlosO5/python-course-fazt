
mystr = "hello world"

print("My name is " + mystr)
print("My name is {mystr}")
print("My name is {0}".format(mystr))

#print(dir(mystr))  # El metodo dir muestras todas las funciones a utilizar con el dato

print(mystr.upper()) # Todo en mayuscula
print(mystr.lower()) # Todo en minuscula
print(mystr.swapcase()) # Todo en mayuscula
print(mystr.capitalize()) # #Primera letra en mayuscula
print(mystr.replace("hello", "bye")) # Cambiar palabra
print(mystr.count("o"))  # Conteo de letras


print(mystr.startswith("hello"))  # Devuelve true o false
print(mystr.endswith("world"))  # Devuelve true o false


print(mystr.split("o"))  # Dividir el texto en 2
print(mystr.find(" "))  # Entrega el indice del item

print(len(mystr))  # longitud de la variable
print(mystr.index("e"))  # Buscar indice del item


print(mystr.isnumeric())  # Saber si el item es numerico
print(mystr.isalpha())  # Saber si el item es alfanumerico

print(mystr[4])  # Ver el item del indice
print(mystr[-4])  # Ver el item del indice







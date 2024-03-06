
demo_list = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']


numbers_list = list((1, 2, 3 , 4))
# print(numbers_list)

r = list(range(1, 10)) # Metodo para imprimir un ranco de numeros

print(r)
print(len(colors)) # Indice de la longitud de la lista

print('green' in colors) # Devuleve verdadero o falso (dependiendo si el color esta o no en la lista)

colors[1] = 'yellow'
print(colors)

colors.append('violet') #El metodo append solo toma un elemento
colors.extend(['black', 'pink']) # El metodo extend permite introducir varios elementos
colors.insert(-1, 'violet') # Insertar un elemento
colors.pop() # Quitar un elemeto
colors.remove('red') # Remueve el elemento
colors.clear() # Linpia la lista pero no la borra

colors.sort() # Ordenar alfaveticamente
colors.sort(reverse=True) # Ordenar a inversa
colors.index('blue') # Ordenar a inversa
colors.count('red') # Cuenta cuantas veces esta el intem en la lista














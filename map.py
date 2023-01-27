# Para limpiar la shell cuando se ejecute
import os 
os.system('clear')

# forma clasica de transformar valores de una lista sin map
numbers = [1,2,3,4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)
print(numbers)
print(numbers_v2)

# forma eficiente de hacer el mismo ejercicio usando "Map"
numbers = [1,2,3,4]
numbers_v2 = []

# con map puedo manderle ya sea una funcion o una lambda, no hay problema 
numbers_v2 = list(map(lambda i : i * 2, numbers))
print(numbers_v2)

# podemos usar map para sumar listas de diferentes longitudes
numbers_1 = [1,2,3,4]
numbers_2 = [5,6,7]
print(f'Lista 1 de numeros: {numbers_1}')
print(f'Lista 2 de numeros: {numbers_2}')

# aca dara como resultado una lista con las sumas pero con la longitud de la lista más corta
result = list(map(lambda x, y : x + y, numbers_1, numbers_2))
print(result)



"""IMPORTANTE, en tu carrera como Data Scientist trabajaras muchas veces con "Maps" y en vez de usar datos simples como "ints" o "strings" la mayoria de veces procesaros datos dentro de 'Dictionaries'"""

# Ejemplo de un compañero para usar la función map() y usando tuplas como objetos iterables, se pone el nombre de la función mas esta no se tiene que ejecutar

def ingredientes(a, b):
  return a + " es a " + b

menu = list(map(ingredientes, ('carne', 'maiz', 'aguacate'), ('molida', 'tacos', 'guacamole')))

print(list(menu))
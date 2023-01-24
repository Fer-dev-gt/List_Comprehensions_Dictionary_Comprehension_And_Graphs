import os                                               # Para limpiar la shell cuando se ejecute
import csv                                              # Primero importamos un modulo nativo que tiene Python para leer archivos CSV
os.system('clear')

"""                                                     # Mostramos los datos fila a fila                                        
                                                        # Creamos una funcion que se ejecuta con if __name__... y usamos "with open()"" ademas de funciones del modulo csv                                  
  def read_csv(path):                                   # El parametro "path" es donde esta ubicado nuestro .csv 
    with open(path, 'r') as csvfile:                    # Usamos funcion "with open()" y le damos un alias "csvfile"
      reader = csv.reader(csvfile, delimiter = ',')     # Creamos un "reader" dandole como parametro el alias y usamos un delimitador ',' dependiento de como este en el .csv   
      for row in reader:                                # Por cada fila en el "reader"
        print('***' * 12)
        print(row)                                      # Mostramos los datos como de cada fila y los muestra como una lista"""  

    
def read_csv(path):                                     # Mostramos los datos como una lista de diccionarios, donde la llave es el nombre de la columna para mostrar los valores
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')       # Creamos un "Reader"
    header = next(reader)                               # Guardamos los nombres de las columnas
    data = []                                           # Creamos una lista vacia

    for row in reader:
      iterable = zip(header, row)                                         # Usando la funcion "zip()" creamos un diccionario uniendo el nombre de las columnas (header) con todas las filas (row)
      #print(list(iterable))                                              # Imprime listas de pares llave-valor en forma de tupla
      
      country_dictionary = {key : value for key, value in iterable}       # Convertimos a un formato diccionario usando "dictionary comprehension" usando "iterable" 
      data.append(country_dictionary)                                     # A la lista vacia "data" le agregamos al final todos los valores de las filas con los nombres de las columnas
      
    return data                                                           # Retornamos la lista con el formato deseado (lista de Diccionarios)
      
  
if __name__ == '__main__':                                                # Con esto nos aseguramos que el programa se ejecute como un script desde la terminal
  data = read_csv('./data.csv') 
  print(data[0:9])                                                        # Imprimimos el pais o paises (valor) deseados de la lista de paises
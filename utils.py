"""Este archivo servira como modulo de otro programa, el cual lo importara al escribir el nombre del archivo usando 'Import'"""

def get_population(country_dictionary):
  population_dictionary = {                               # Creamos un nuevo diccionario de la poblacion en ciertos años
    '2022' : int(country_dictionary['2022 Population']),
    '2020' : int(country_dictionary['2020 Population']),
    '2015' : int(country_dictionary['2015 Population']),
    '2010' : int(country_dictionary['2010 Population']),
    '2000' : int(country_dictionary['2000 Population']),
    '1990' : int(country_dictionary['1990 Population']),
    '1980' : int(country_dictionary['1980 Population']),
    '1970' : int(country_dictionary['1970 Population']),
  }
  labels = population_dictionary.keys()                   # Guardamos las llaves de los nombres de los paises
  values = population_dictionary.values()                 # Guardamos los valores de la poblacion del pais
  
  return labels, values                                   # Retornamos los nombres de los paises y su poblacion


A = 'Hola'                                                # Creamos una variable que la usara el otro archivo, pero la mayoria de veces solo importamos funciones

def population_by_country(data, country):                                             # Creamos una funcion que muetra la población de un pais
  result = list(filter(lambda item : item['Country/Territory'] == country, data))     # Filtramos de entre la lista en "data" al pais ingresado en "country"
  return result                                                                       # Retoramo los valores filtrados
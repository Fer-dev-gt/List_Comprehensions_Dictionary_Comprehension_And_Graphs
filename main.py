import os                                   # Para limpiar la shell cuando se ejecute
import utils                                # Importamos modulos que creamos en otros archivos
import read_csv                             # Importamos module "read_csv" con datos en formato correcto
import charts                               # Modulo para graficar                           

os.system('clear')                          # Limpia la terminal cada vez que se inicia un programa


def run():
  data = read_csv.read_csv('./data.csv')                                            # Usamos module "read_csv", usamos funcion "read_csv" y pasamos como parametro la base de datos

  data = list(filter(lambda item : item['Continent'] == 'South America', data))     # Filtramos a los paises que son de "South America", "data" es el iterable (lista de diccionarios)
  countries = list(map(lambda x : x['Country/Territory'], data))
  percentages = list(map(lambda x : x ['World Population Percentage'], data))

  charts.generate_pie_chart(countries, percentages)                                 # Generamos grafica de pastel con datos de "countries" y "percentages" usando el modulo "charts.generate_pie_chart"
  
  """
  country = (input('Type Country => ')).capitalize()
  result = utils.population_by_country(data, country)         # Invocamos funcion para obtener pais ingresado

  if len(result) > 0:                                         # Nos aseguramos que la lista no este vacia
    country = result[0]                                       # Guardamos el nombre del pais de la lista
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)                 # Generamos grafica
  
  #print(utils.A)                                             # Incluso si se trata de una variable, esta la podemos importar de la misma manera que con una funcion
  #print(result)"""


if __name__ == '__main__':                                    # Entry Point
  run()
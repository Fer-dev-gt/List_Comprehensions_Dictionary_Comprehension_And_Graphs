import os                                                 # Para limpiar la shell cuando se ejecute
import matplotlib.pyplot as plt                           # Importamos del modulo "matplotlib" la funcion "pyplot", viene incorporado en Python, luego le damos una alias "plt"
os.system('clear')


def generate_bar_chart(labels, values):                   # Con esta función generamos la grafica de barras
  fig, ax = plt.subplots()
  ax.bar(labels, values)                                  # Los parametros pueden ser enviados desde otro modulo "main.py" o desde el modulo local
  plt.show()                                              # Mostramos la gráfica


def generate_pie_chart(labels, values):                   # Con esta función generamos la grafica de pie
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)                         # Le mandamos la informacion que va a usar esta grafica
  ax.axis('equal')
  plt.show()                                              # Mostramos la gráfica
  

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  #generate_bar_chart(labels, values)                     # Invocamos funcion para crear grafica de barras
  generate_pie_chart(labels, values)                      # Invocamos funcion para crear grafica de pastel
import os                          # Para limpiar la shell cuando se ejecute
import main                        # Podemos importar datos de otros archivos como "main" en este caso    
os.system('clear')

print(f'Example => {main.data}')   # Imprimimos una variable que pertenece al modulo "main"

main.run()                         # Para no ejecutar todo el codigo del archivo 'main' cuando lo importamos, aislamos parte del codigo en la funcion run(), asi podemos traer variables sin problemas



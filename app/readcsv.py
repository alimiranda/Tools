import csv

def read_csv(path):  # creo una función cuyo parámetro d3 entrada es la ruta del archivo que posteriormente leeré
   with open(path,'r') as csvfile: # Abro el archivo y lo nombro csvfile
      reader = csv.reader(csvfile,delimiter=',') # creo una variable que lee el archivo separado por comas
      header = next(reader) # Como reader es un iterable, busco el header de cada columna
      data=[] # creo una lista vacía donde posteriormente quedaran mis datos organizados por pais
      for row in reader: # Cada fila corresponde a un país
         iterable = zip(header,row) # Creo un iterable que une en formato tupla el header y el valor de cada fila en pares
         #print(list(iterable))
         country_dict = {key:value for key, value in iterable} # Hago un diccionario con las parejas creadas en iteraable donde header es el key y el value es el valor correspondiente en la fila recorrida
         print(country_dict)
         data.append(country_dict) # Voy agregando cada diccionario a la lista "data"
      print(data)
      return data # la función retorna la lista de diccionarios con la información por país


if __name__=='__main__':
   read_csv('/Users/alinasofiamirandamartinez/Documents/1_Datos/world_population.csv')

   #print(sys.path)
   
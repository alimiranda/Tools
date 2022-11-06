
#### Para agragar líneas con el r+ ###
with open('./text.txt','r+') as file:
   for line in file:
      print(line)
   file.write('Nuevas cosas\n')
   file.write('Otra línea\n')

#### Para reemplazar el contenido w+ ###
with open('./text.txt','w+') as file:
   for line in file:
      print(line)
   file.write('Nuevas cosasReemplazando\n')
   file.write('Otra línea Reemplazando\n')
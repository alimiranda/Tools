file = open('./text.txt')

'''#print(file.read())

print(file.readline())
print(file.readline())

file.close()'''

'''for line in file:
   print(line)

file.close()'''

with open('./text.txt') as file:
   for line in file:
      print(line)
   

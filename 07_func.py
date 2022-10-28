def my_print(text):
   print(text + text*2)

my_print("Hola, cualquier texto")

def sum_with_range(min,max):
   print(min, max)
   sum = 0
   for x in range(min,max):
      sum += x
   
   return sum
   

result = sum_with_range(1,20)
print(result)
numbers = [1,2,3,4]
numbers_v2 = []

numbers_v2 = [i * 2   for i in numbers]

print (numbers_v2)

numbers_v3 = list(map(lambda i : i*3,numbers))

print (numbers_v3)

numbers_2 = [1,2,3,4]
numbers_3 = [5,6,7]

result = list(map(lambda x,y:x+y,numbers_2, numbers_3))

print (result)
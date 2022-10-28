def increment(x):
   return x+1

increment_v2 = lambda x : x + 1
result = increment_v2(10)

print (result)

full_name = lambda name, last_name: f'Full name es {name.title()}{last_name.title()}'

text = full_name('nicolas', 'perez casas')
print(text)
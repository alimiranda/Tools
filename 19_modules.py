import sys
import re
import time
import collections

print(sys.path)

text = 'Mi numero de telefono es 305252619, el codigo del apis es 57, mi numero de la suerte es 4'
result = re.findall('[0-9]+',text)
print(result)

timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

numbers = [1,2,1,2,3,4,3,4,5,4,6]
counter = collections.Counter(numbers)
print(counter)

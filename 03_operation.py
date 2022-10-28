set_a = {'col','mex','bol'}
set_b = {'pe','bol'}

set_c = set_a.union(set_b)
print (set_a | set_b)
print(set_c)

set_d = set_a.intersection(set_b)
print (set_a & set_b)
print(set_d)

# Diferencia

set_e = set_a.difference(set_b)
print (set_a - set_b)
print(set_e)

# Diferencia simétrica (unión sin los elementos en común)

set_f = set_a.symmetric_difference(set_b)
print (set_a ^ set_b)
print(set_f)
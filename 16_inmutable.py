items = [
   {
      'product': 'camisa',
      'price':100
   },
   {
      'product': 'pantalon',
      'price':200
   },
   {
      'product': 'pantaloneta',
      'price':300
   }
]


prices = list(map(lambda items : items['price'], items))

print(prices)

def add_taxes(item):
   new_list=item.copy()
   new_list['taxes'] = new_list['price']*.19
   return new_list
new_items = list (map(add_taxes,items))

print(new_items)
print(items)
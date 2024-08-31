# dictionary


capitals = {

'USA': 'Washinton DC',
'India': 'New Dehli',
'China': 'Beujing',
'Russia': 'Moscow'
}


capitals.update({'Germany': 'Berlin'})
capitals.update({'USA', 'Las vegas'})
capitals.pop('China')

#print(capitals['Germany'])
# print(capitals.get('Germany'))

print(capitals.keys())
print(capitals.values())
print(capitals.items())


for key,value in capitals.items():
  print(key, value)
# slincing = create a substring by extrancting elements from another string

# indexing[] or slice()
# [start:stop:step]

name = "Gabriel oliveira"

first_name = name[:7]
last_name = name[8:16]
full_name = name[::2]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(full_name)
print(reversed_name)

website = "http://google.com"

slice = slice(7, -4 )

print(website[slice])
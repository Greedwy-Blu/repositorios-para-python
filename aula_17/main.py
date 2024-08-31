# set = collection which unordered, unidexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl","plate","cup","knife"}


utensils.add("napkin")
utensils.remove("fork")
utensils.update(dishes)

dinner_table = utensils.union(dishes)

for x in utensils:
  print(x)

  for i in dinner_table:
    print(i)


print(dishes.difference(utensils))

print(utensils.intersection(dishes))
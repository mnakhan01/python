from employee import employee

employee1 = employee("mark","customer","rep")
employee2 = employee("fisher","it","manager")

print(employee1.title)
print(employee2.name)
print(employee2.is_bonus_eligible())

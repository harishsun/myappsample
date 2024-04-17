# This program is for sorting a list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Reverse sorting a list

cars.sort(reverse = True)

print(cars)

cars  = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)


# sorted

print(f"\nHere is the sorted list {sorted(cars)}")
print(f"\nHere is the original list{cars}")

# We can also reverse the order without using the sort method

cars.reverse()

print(cars)

# Finding the length of the list

total_elements = len(cars)
print(total_elements)



# Exercise 3-8
locations = ['india', 'london', 'japan', 'switzerland']
print(locations)
print(sorted(locations))
print(f"Original list: {locations}")
original_list = locations
locations.sort(reverse=True)
print(locations)
locations.reverse()
print(locations)
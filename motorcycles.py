# Modifying elements in the list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Appending elements to the list

motorcycles.append('honda')
print(motorcycles)


# Inserting elements to the list

motorcycles.insert(0, 'harley')

print(motorcycles)

del motorcycles[0]
print(motorcycles)

# Remove an item from the list and use it for other list or something else  - POP
 
popped_motorcycles = motorcycles.pop()

print(motorcycles)
print(popped_motorcycles)


motorcycles.insert(0, popped_motorcycles)
print(motorcycles)
first_owned = motorcycles.pop(0)

print(f"My first owned motorcycle was {first_owned}")

too_expensive = 'ducati'

motorcycles.remove(too_expensive)

print(f"\nA {too_expensive.title()} is too expensive for me.")

print(motorcycles)

print(motorcycles[2]) # This error was made intentionally to understand Index error

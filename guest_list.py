# Exercise 3-4, 3-5, 3-6 and 3-7

guests = ['musk', 'enstein', 'tesla']

print(f"Mr. {guests[0].title()} i would like to formally invite you for a tech talk dinner!")
print(f"Mr. {guests[1].title()} i would like to formally invite you for a tech talk dinner!")
print(f"Mr. {guests[2].title()} i would like to formally invite you for a tech talk dinner!")

guest_cancelled = guests.pop(1)
replacement_guest = guests.insert(1, 'jobs')
print("\n")

print("\n")

print(f"Mr. {guests[0].title()} i would like to formally invite you for a tech talk dinner!")
print(f"Mr. {guests[1].title()} i would like to formally invite you for a tech talk dinner!")
print(f"Mr. {guests[2].title()} i would like to formally invite you for a tech talk dinner!")

print("\n")

print(f"Sorry, this is to let you know that Mr.{guest_cancelled.title()} cannot make it for the dinner.")

guest_cancelled = guests.pop(1)

print(f"Sorry, this is to let you know that Mr.{guest_cancelled.title()} cannot make it for the dinner.")

print(f"Guests attending dinner are Mr.{guests[0].title()} and Mr.{guests[1].title()}")


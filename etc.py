str1 = 'alpha'
str2 = 'beta'
str3 = '''gamma string'''
num1 = 123
first_list = [str1, "DevOps", 47, num1, 1.5]

print(first_list)

first_tuple = (str1, "DevOps", 47, num1, 1.5)

print(first_tuple)

first_dictionary = {"Name":"Harish", "weight":75, "Exercises": ["Boxing", "walking", "Dancing"]}

listinDict = first_dictionary.get("Exercises")
print(listinDict[0])

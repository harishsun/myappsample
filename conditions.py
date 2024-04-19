#This code will check for conditions inside tuple, list and dictionary

print("This IT Organization has vatrious skill sets")
print("Find out your match.")

print("Enter Capitalised Values:")

DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "rush", "Java", "C#")
cntr_emp1 = {"Name":"Santa", "Skill":"Blockchain", "Code":1024}
cntr_emp2 = {"Name":"Rocky", "Skill":"AI", "Code": 1218}

usr_skill = input("Enter your desired skill: ")

#Check from the database if we have the desired skill

if usr_skill in DevOps:
    print(f"we have {usr_skill} in DevOps Team.")
elif (usr_skill in Development):
    print(f"We have {usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees in  {usr_skill} skill.")
else:
    print("Skill not found")
    print("Please check if you have entered the correct uppercase and lowercase letters")

""" we are going to write a program which will select a random name from a list of names.
The person selected will have to pay for everybody's food bill."""


import random
names_string = (input("Give me everybody's names, separated by a comma. \n"))
names = list(names_string.split(","))
length=len(names)
choose=random.randint(0,length-1)
selected_person=names[choose]
print(f"{selected_person} is going to buy the meal today!")



"""You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails"."""
import random
print("Hey User! you can start toosing")
user=random.randint(0,1)
if user== 1:
    print("Head")
else:
    print("Tail")
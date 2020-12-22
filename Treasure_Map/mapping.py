"""You are going to write a program which will mark a spot with an X.
 write a program that allows you to mark a smile on the map using a two-digit system.
 The first digit is the vertical column number and the second digit is the horizontal row number.
"""

row1 = ["😄️","😄️","😄️"]
row2 = ["😄️","😄️","😄️"]
row3 = ["😄️","😄️","😄️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

row=int(input("Enter the row value"))
column=int(input("Enter the column value"))

map[row-1][column-1]='👍'

print(f"{row1}\n{row2}\n{row3}")
#9.5

with open("number1to10.txt", "w") as file:
    for i in range(1, 11):
        file.write(str(i) + "\n")

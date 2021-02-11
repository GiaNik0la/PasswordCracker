import itertools

print("Recomended only 10 info... not less")

print(" ")
print(" ")
print(" ")
print(" ")
lines = []
Name = input("Enter .txt Name: ")

file1 = open(f'{Name}.txt', 'r') 
Lines = file1.readlines()

for i in Lines: lines.append(i.rstrip())

l1 = lines[0]
l2 = lines[1]
l3 = lines[2]
l4 = lines[3]
l5 = lines[4]
l6 = lines[5]
l7 = lines[6]
l8 = lines[7]
l9 = lines[8]
l10 = lines[9]

crack = list(itertools.product([l1, l2, l3, l4, l5, l6, l7, l8, l9, l10],repeat=3))

document = open("Passwords.txt", "w")
document.write(f"""{str(crack)}
""")
document.close()
for i in crack: print(f"{crack}", " ")

    
    

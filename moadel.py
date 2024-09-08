tedad_danehs = int(input("Enter your many of student:"))

list_nomre = [] # list()

for i in range(tedad_danehs):
    nomre = float(input(f"Eneter the mark {i+1}: "))
    
    list_nomre.append(nomre)

print(list_nomre)
print( len(list_nomre) )
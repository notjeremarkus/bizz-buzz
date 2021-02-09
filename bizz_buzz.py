# Laki1 | Harjoitus 3 | Tehtävä 7
# Jere Salomaa

print("Hello! This is a BizzBuzz simulation.")
print("Please, enter the number of turns:")
vuorot = int(input())

laskuri = 0

for i in range(1, vuorot + 1):
    string = ""
    if i % 3 == 0 and i % 5 == 0:
        string = string + "bizz buzz"
    elif i % 3 == 0:
        string = string + "bizz"
    elif i % 5 == 0:
        string = string + "buzz"
    else:
        string = string + str(i)
        
    laskuri = laskuri + 1
        
    if laskuri < vuorot:
        print(string, end=", ")
        
    else:
        print(string, end=".")
    
print()
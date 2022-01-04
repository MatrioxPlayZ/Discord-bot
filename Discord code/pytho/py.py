citylist=["Rome","New York","Los Angeles","Tokyo"]
choice =""
while choice != "X":
    print("=========================")
    print("C I T Y  L I S T E R 5000")
    print("=========================")
    print("Choose what you want to do:")
    print("A: Print the list")
    print("B: Remove a City")
    print("C: Add a City")
    print("D: Search for a city")
    print("E: Sort the list")
    print("F: Print a singular element")
    print("X: Exit the list")

print("Enter your choice:")
if choice == "A":
    print(citylist)

if choice == "B":
    i=input("which city do you want to remove?")
    i=int(i)
    del citylist[i]
    print(i, "has been removed from the list")

if choice == "C":
    new=input("Input a new city")
    citylist.append(new)
    print(new, "has been added to the list")

if choice == "D":
    name= input("Enter a search term: ")
    stop= len(citylist)
    for i in range(stop):
        if citylist[i] == name:
            print(name, "Found in the list")

if choice == "E":
    citylist.sort()
    print(citylist)

if choice == "F":
    i= input("which list item do you want to print?")
    i= int(i)
    print(citylist[i])
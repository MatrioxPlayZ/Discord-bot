atoms = ["Carbon", "Hydrogen", "Helium", "Berylium", "Boron", "Nitrogen", "Oxygen", "Flourione", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Potassium", "Cobalt", " Nickel", "Radon"]

choice =""
while choice != "X":
    print("====================================")
    print("ATOM FINDER")
    print("====================================")
    print("\n")
    print("A: Append a atom to the list")
    print("B: Remove a atom from the list")
    print("C: Print the list")
    print("D: Search for a item in the list")
    print("X: Exit the program")
    print("\n")
    choice =input("Chhose an option: ")\

    if choice == "A":
            name = input("Enter the name of the atom to add: ")
            atoms.append(name)
            print(name,"Has been added to the list.")

    if choice == "B":
            name = input("enter the name of the atom to remove: ")
            atoms.remove(name)
            print(name,"The atom has been removed from the list")

    if choice == "C":
            print(atoms)

    if choice == "D":
        name = input("Enter a search term: ")
        stop = len(atoms)
        for i in range (stop):
                if atoms[i] == name:
                        print(name,"was found in the list")



                if choice =="X":
                        quit()

coca = 20
sabritas = 15
def takeDesition():
    x = 1
    while x ==1:
        desition = int(input("What do you want to buy? (1,2):\n"))
        if desition == 1 or desition == 2:
            x = 2
        else:
            print("Invalid input.")
        
    return desition
def howMany():
    x = 1
    while x ==1:
        quantity = int(input("How many?\n"))
        if quantity <= 0:
            print("Invalid answer.")
        else:
            x = 2
    
    return quantity

menu = """

                MENU
        1. COCA
        2. SABRITAS

"""
print(menu)
flag = 1
while flag == 1:
    desition = takeDesition()
    if desition == 1:
        desition = coca
    elif desition == 2:
        desition = sabritas
    quantity = howMany()
    total = desition * quantity
    print("Your total will be", total,"\n")
    flag = int(input("Do you want to buy something else? (1 = yes/ 2 = no)\n"))


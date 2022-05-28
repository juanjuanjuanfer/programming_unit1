
def sum(num1,num2):
    print(num1 + num2)
    return 
def substract(num1,num2):
    print(num1 - num2)
    return 
def multiply(num1, num2):
    print(num1*num2)
    return 
def divide(num1,num2):
    print(num1/ num2)
    return 

loop = 1
while loop == 1:
    desicion = int(input("Select an option\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n"))
    
    if desicion ==1:
        num1 = int(input("Type number 1: \n"))
        num2 = int(input("Type number 2: \n"))
        sum(num1,num2)
    elif desicion == 2:
        num1 = int(input("Type number 1: \n"))
        num2 = int(input("Type number 2: \n"))
        substract(num1,num2)
    elif desicion == 3:
        num1 = int(input("Type number 1: \n"))
        num2 = int(input("Type number 2: \n"))
        multiply(num1,num2)
    elif desicion == 4:
        num1 = int(input("Type number 1: \n"))
        num2 = int(input("Type number 2: \n"))
        divide(num1,num2)
    else:
        print("invalid input")
    otra = input("Let's do next calculation?(yes/no)\n")
    if otra == "yes":
        loop = 1
    elif otra == "no":
        loop = 2
    else:
        print("invalid answer, bye")
        loop =2
    



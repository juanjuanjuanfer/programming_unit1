#Import libraries 
import math

#Declare the functions
    
#Function menu() show the menu is screen and selects an option.
def menu():
    print("Welcome, please choose an option:\n")
    m = True
    while m == True:
        opt = int(input("1. Polar form of a complex number.\n2. Magnitude and direction of a vector.\n"))
        if opt == 1:
            polarForm()
        elif opt == 2:
            magnitudeAndDirection()
        else:
            h=2
            while h != 1:
                opti = int(input("That is not a valid option, please try again.\n"))
                if opti == 1:
                    polarForm()
                    h = 1
                elif opti == 2:
                    magnitudeAndDirection()
                    h = 1
        cont = input("\nDo you want to do something else? (yes/no)\n")
        if cont == "yes":
            m = True
        else:
            m = False
            
    return

def polarForm():
    i = float(input("\n\t|||POLAR FORM OF A COMPLEX NUMBER|||\n\nType the real number:\n"))
    a = float(input("Type the imaginary number's coeficient:\n"))
    semir = (a**2)+(i**2)
    r = "sqrt(" + str(semir) + ")"
    if a == 0 or i ==0 :
        if i == 0:
            if a > 0:
                tangente = 0.0
                printresult(a,i,r,tangente)
            elif a < 0:
                tangente = 180.0
                printresult(a,i,r,tangente)                
        elif a == 0:
            if i > 0:
                tangente = 90.0
                printresult(a,i,r,tangente)                
            elif i < 0:
                tangente = 270.0
                printresult(a,i,r,tangente)              
    else :             
        if i < 0 and a > 0:
            tangente = 180 - math.degrees(math.atan2(abs(a),abs(i)))
            printresult(a,i,r,tangente)            
        elif i < 0 and a < 0:
            tangente = 180 + math.degrees(math.atan2(abs(a),abs(i)))
            printresult(a,i,r,tangente)    
        elif i > 0 and a < 0:
            tangente = 360 - math.degrees(math.atan2(abs(a),abs(i)))
            printresult(a,i,r,tangente)
        elif i > 0 and a > 0:
            tangente =  math.degrees(math.atan2(abs(a),abs(i)))
            printresult(a,i,r,tangente)           

def magnitudeAndDirection():
    print("\n\t|||MAGNITUDE AND DIRECTION OF A VECTOR|||\n\n")
    i = float(input("Type i: "))
    j = float(input("Type j: "))
    magnitude2 = (i**2) + (j**2)
    if i == 0 or j ==0 :
        if j == 0:
            if i > 0:
                tangente = 0.0
                printresultado(magnitude2,tangente)
            elif i < 0:
                tangente = 180.0
                printresultado(magnitude2,tangente)
                
        elif i == 0:
            if j > 0:
                tangente = 90.0
                printresultado(magnitude2,tangente)
                
            elif j < 0:
                tangente = 270.0
                printresultado(magnitude2,tangente)
              
    else :             
        if i < 0 and j > 0:
            tangente = 180 - math.degrees(math.atan2(abs(i),abs(j)))
            printresultado(magnitude2,tangente)            
        elif i < 0 and j < 0:
            tangente = 180 + math.degrees(math.atan2(abs(i),abs(j)))
            printresultado(magnitude2,tangente)    
        elif i > 0 and j < 0:
            tangente = 360 - math.degrees(math.atan2(abs(i),abs(j)))
            printresultado(magnitude2,tangente)
        elif i > 0 and j > 0:
            tangente =  math.degrees(math.atan2(abs(i),abs(j)))
            printresultado(magnitude2,tangente)
    return
    
    return

#Function 'printresult()' prints the result with the given parameters.           
def printresult(a,i,r,tangente):
    print("The polar form of (",i ,",", a,"i ) is: \n" , r, "( cos", tangente, "+ isen", tangente,")\n")

def printresultado(magni,direc):
    print("The magnitude is sqrt(", magni,") and the angle is", direc)
    return
#Code is executed by calling the main function and then the selected option.

menu()
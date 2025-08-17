#functions of calculator
def add(a,b):
    return a + b
def multiply(a,b):
    return a * b
def subtract(a,b):
    return a - b
def divide(a,b):
    return a / b
def modulus(a,b):
     return a % b


#choices
print("select your operation:")
print("1. Add:")
print("2. Multiply:")
print("3. Subtract:")
print("4. Divide:")
print("5. Modulus:")

#conditions
while True:
    choice = input("enter 1/2/3/4/5:")
    
    if choice in ('1', '2', '3', '4','5'):
        try:
            a=float(input("enter value of a:"))
            b=float(input("enter value of b:"))
        except ValueError:
            print("invalid input please input correct choice-->")
            continue

        if choice == "1":
                print ( a,"+", b ," =" , add(a,b))
        elif choice == "2":
                print ( a,"*",b , "=" , multiply(a,b))
        elif choice == "3":
                print ( a,"-",b, "=" , subtract(a,b))
        elif choice == "4":
            try:
                print ( a,"/",b, "=" , divide(a,b))
            except ZeroDivisionError:
                print("cannot divide by zero!!")
        elif choice == "5":
                
                     print ( a,"%",b, "=" , modulus(a,b))
                
        next_calculation=input("next calculation? (yes/no):")
        if next_calculation== "no":
            print("Thank you & Have a good day \u2665!!")
            break
    else:
        print("invalid input")


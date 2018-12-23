num1 = input("enter num1")
num2 = input("enter num2")
operation = input("enter operator")
def calc(num1,num2,operation):

    if (operation== '+'):
        return float(num1) + float(num2)
    elif (operation== '-'):
        return float(num1) - float(num2)
    elif (operation== '*'):
        return float(num1) * float(num2)
    elif (operation== '/'):
        return float(num1) / float(num2)
print(calc(num1,num2,operation))


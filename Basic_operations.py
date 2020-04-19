#This program will take two input of two numbers
#Author Rida Hamid

operand = int(input("Enter  your first digit: "))
operand2 = int(input("Enter  your second digit: "))
operation=input("Enter your operator 1:Addition 2:Subtraction 3:Multiplication 4:Division ")
if operation == '1':
    print('addition:  ' ,  operand + operand2)
elif operation == '2':
    print('subtraction: ' , operand - operand2)
elif operation =='3':
    print('multiplication: ', operand * operand2)
elif operation == '4':
    print('division:' , operand / operand2)

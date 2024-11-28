def numbers():
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    return num1,num2
def calculate_sum(num1,num2):
    add=num1+num2
    return add
def display(call):
    print(f"the addition of two numbers is:{call}")
num1,num2=numbers()
call=calculate_sum(num1,num2)
display(call)
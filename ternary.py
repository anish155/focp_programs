a=int(input("input first number:"))
b=int(input("input second number:"))
c=int(input("input third number:"))
largest= a if a>b and a>c else b if b>c else c 
print(largest)
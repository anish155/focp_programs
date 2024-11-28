'''natural=int(input("enter the number:"))
natural_number=natural*(natural+1)/2
print(natural_number)'''


n=int(input("enter the number"))
b=0
i=1

while i<=n:
 c=i**2
 print(f"the sum of square of first {n} number is:{c}")
 b+=c
 i+=1
print(f"{b}")



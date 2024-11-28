'''rows=int(input("enter the number:"))
for a in range(rows):
    for b in range (a+1):
        print("*",end="")

    print()'''



i=1
while i<=5:
    print("1"*i)
    i+=1

i=1
while i<=5:
    pattern=(10**i-1)//9
    pattern=pattern*pattern
    print(pattern)
    i+=1

i=5
while i>=1:
    print(f"{i}"*i)
    i-=1
i=1
while i<=5:
    pattern=(10**i-1)//9
    pattern=pattern*pattern
    print(pattern)
    i+=1


i=1
while i<=5:
    print(" "*(5-i)+"*"*i)
    i+=1
i=1
while i<=5:
    print(" "*(5-i)+"*"*i)
    i+=1
i=1
while i<=5:
    print(" "*4+"*")
    i+=1

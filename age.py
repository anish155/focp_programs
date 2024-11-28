age=int(input("enter the age:"))
if(age in range(0,3)):
    print("infant")
elif(age in range(3,11)):
    print("children")
elif(age in range(11,18)):
    print("teen")
elif(age in range(18,56)):
    print("adult")
elif(age in range(56,101)):
    print("hajurba")
else:
    print("get out.")



'''day=int(input("enter the number for day:"))
week="sunday"if day==1 else "monday" if day==2 else "tuesday" if day==3 else "wednesday" if day==4 else "thrusday" if day==5 else "friday" if day==6 else "saturday" if day==7 else "number error"
print(week)'''
number=int(input("enter the number:"))
weeks=["sunday","monday","tuesday","wednesday","thrusday","friday","saturday"]
print(weeks[number-1]) if 0<number<8 else print("invalid number")


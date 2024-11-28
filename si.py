principal=float(input("enter principal:"))
year=int(input("enter year:"))
month=int(input("enter month:"))
time=float((month/12)+year)
rate=float(input("enter rate:"))
print(f" time is :{time}" ) 
simple_interest=(principal*time*rate)/100
print(f"the simple interest is {simple_interest}.")
'''you can also put time in months or use by float.'''
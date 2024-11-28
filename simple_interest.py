def principal():
    p=int(input("enter principal:"))
    return p
def time():
    t=int(input("enter time:"))
    return t
def rate():
    r=int(input("enter rate:"))
    return r
def simple_interest(p,t,r):
    si=(p*t*r)/100
    return si
def display(call):
    print(f"the simple interest is:{call}")
p=principal()
t=time()
r=rate()
call=simple_interest(p,t,r)
display(call)
names=["ram","hari","shyam","rita"]
name=input("enter your name:")
for n in names:
    if n==name:
        print(f"found {name}")
        break
else:
    print("didnot found")
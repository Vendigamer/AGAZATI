x = int(input("x="))
y = int(input("y="))

if x < y:
    for i in range(x,y+1):
        x = x*i
    print(f"{x}")
elif y < x:
    print("Y nagyobb mint X")
elif x == y:
    print(f"{x*x}")
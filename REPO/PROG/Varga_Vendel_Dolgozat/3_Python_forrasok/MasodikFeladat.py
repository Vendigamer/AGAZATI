import math
x = 0

while x != 4:
    u = input("u=")
    a = input("a=")
    s = input("s=")
    v = input("v=")
    try:
        u2 = float(u)
        x += 1
    except:
        print("A bevitt adatok valamelyike hibás!")
    try:
        a2 = float(a)
        x += 1
    except:
        print("A bevitt adatok valamelyike hibás!")
    try:
        s2 = float(s)
        x += 1
    except:
        print("A bevitt adatok valamelyike hibás!")
    try:
        v2 = float(v)
        x += 1
    except:
        print("A bevitt adatok valamelyike hibás!")

Szam = round(u2 + math.sqrt(2*a2*s2),2)
print(f"A végsebesség: {Szam} ")


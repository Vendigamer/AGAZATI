import math


while True:
    try:
        m = float(input("m="))
        v = float(input("v="))
        try:
            x = (((math.sqrt(math.sqrt(m+v)*math.pi))/(2*math.pi))**(8/5))*(1/2*v)
            print(f"{x:.2f}")
            break
        except:
            print("Hibás adat!")
    except:
        print("Hibás adat!")

from math import cos, radians, sqrt

a = float(input("Skriv in sidan A's längd: "))
b = float(input("Skriv in sidan B's längd: "))
v = float(input("Skriv in sidan A's vinkel i grader: "))


v_rad = radians(v)


a_squared = a ** 2
b_squared = b ** 2
twoab_cosv = 2 * a * b * cos(v_rad)


c_squared = a_squared + b_squared - twoab_cosv
c = sqrt(c_squared)


c_int = int(c)


if c > a and c > b:
    print("Triangeln är oliksidig")
  
elif c == a and c == b:
    print("Triangeln är liksidig") 

elif c == a or c == b:
    print("Triangeln är likbent")
  
else:
    print("Felaktiga värden, kontrollera inmatningen.")

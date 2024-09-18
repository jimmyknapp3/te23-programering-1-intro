r = input("Skriv in cirkelns radie ")
r_int = int(r)
if r_int > 0:
    circumference = r_int * 6.28318530718
    print(circumference)
else:
    print("Error, ogiltigt nummer!")

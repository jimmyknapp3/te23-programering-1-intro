användare = input("Hur många minuter pratar du i mobil per månad?")
användare_int = int(användare)
if användare_int < 33:
    print("Du borde köpa Kontant")
elif användare_int > 66:
    print("Du borde köpa Plus")
else:
    print("Du borde köpa Normal")
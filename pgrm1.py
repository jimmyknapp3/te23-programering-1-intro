from math import *
print("Välj vilket talesätt du ska använda genom att skriva ett nummer 1-6")
math = input("Addition 1\nmultiplikation 2\ndivision 3\nkvadratroten 4\nupphöjning 5\nsubtraktion 6\n")
if math == "1":
    num1 = input("Skriv ett nummer:")
    num2 = input("Skriv ett till nummer:")
    result = float(num1) + float(num2)
    print(result)

elif math == "6":
    num1 = input("Skriv in ett nummer:")
    num2 = input("Skriv in ett till nummer:")
    result = float(num1) - float(num2)
    print(result)

elif math == "3":
    num1 = input("Skriv in ett nummer:")
    num2 = input("Skriv in ett till nummer:")
    result = float(num1) / float(num2)
    print(result)
elif math == "4":
    num1 = input("Skriv in ett nummer:")
    result = (sqrt(float(num1)))
    print((result))

elif math == "5":
    num1 = input("Skriv in ett nummer:")
    num2 = input("Skriv ett till nummer:")
    result = float(num1) ** float(num2)
    print (result)







else:
    num1 = input("Skriv in ett nummer:")
    num2 = input("Skriv in ett till nummer:")
    result = float(num1) * float(num2)
    print(result)


while math not in(1, 2, 3, 4, 5, 6):
  print("Välj vilket talesätt du ska använda genom att skriva ett\nnummer 1-6")
  math = input("Addition 1\nmultiplikation 2\ndivision 3\nkvadratroten 4\nupphöjning 5\nsubtraktion 6\n")
  if math == "1":
      num1 = input("Skriv ett nummer:")
      num2 = input("Skriv ett till nummer:")
      result = float(num1) + float(num2)
      print(result)

  elif math == "6":
    num1 = input("Skriv in ett nummer:")
    num2 = input("Skriv in ett till nummer:")
    result = float(num1) - float(num2)
    print(result)

  elif math == "3":
      num1 = input("Skriv in ett nummer:")
      num2 = input("Skriv in ett till nummer:")
      result = float(num1) / float(num2)
      print(result)
  elif math == "4":
      num1 = input("Skriv in ett nummer:")
      result = (sqrt(float(num1)))
      print(round(result))

  elif math == "5":
      num1 = input("Skriv in ett nummer:")
      num2 = input("Skriv ett till nummer:")
      result = float(num1) ** float(num2)
      print (result)







  else:
      num1 = input("Skriv in ett nummer:")
      num2 = input("Skriv in ett till nummer:")
      result = float(num1) * float(num2)
      print(result)
  
from random import randint
rule = input("skriv om ni spelar udda eller jämnt:")
computer = randint(1, 6)
player = randint(1, 6)

if rule == "udda":
    computer_result = computer % 2
    player_result = player % 2
    print(f"datorn rullade {computer_result} och spelaren {player_result}, spelregerln var {rule}")
else:
    print:("jämnt")
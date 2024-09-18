from random import randint

player_one_score = 0
player_two_score = 0
round = 0
run = True

while run:
    round += 1
    player_one_roll = randint(1, 6)
    player_two_roll = randint(1, 6)

    if player_one_roll > player_two_roll:
        print("spelare 1 vann")
        player_one_score += 1
    elif player_two_roll > player_one_roll:
        print("spelare 2 vann")
        player_two_score += 1
    else:
        print("Det blev oavgjort")

    if player_one_score >= 2:
        print("spelare 1 var först att vinna 2 av 3 rundor")
        run = False
    elif player_two_score >= 2:
        print("spelare 2 var först att vinna 2 av 3 rundor")
        run = False     
        

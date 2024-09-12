from random import randint

print("tärningskastspelet")

player_one = randint(1,6)

player_two = randint(1,6)

if player_one > player_two:
    print("1")
    player_one_score = int("1")
elif player_two > player_one:
    print("2")
    player_two_score = int("1")

#totalscore = (player_two_score + player_one_score) 
#print (totalscore)
#while totalscore < 3


    

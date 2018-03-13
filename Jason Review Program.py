new_list = []
print (new_list)

print ("Which Video Game?")

Game_one = "Fortnite"

Game_two = "PUBG"

print (Game_one + "\nor\n" + Game_two)

Video_Game = str(input ("Fortnite Or PUBG?: "))
if Video_Game == Game_two:
    print ("PUBG is a Battle Royal game with a 100 player limit that sells for $29.99")
    print ("-------------")
    print ("PUBG was released Dec 27, 2017")
    print ("Its a FPS, Open world, and Survival game")
    print ("My rating for this game is ") + str(8.5)
else:
    print ("Fortnite is a 100 player Battle Royale for FREE")
    print ("--------------")
    print("Fortnite was released July 25, 2017")
    print ("Its a TPS, Open World, and Survival game")
    print ("My rating for this game is ") + str(4.5)
    
new_list.append(Game_one)
new_list.append(Game_two)
print (new_list)

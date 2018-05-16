# Adventure NBA Game Python Group Project - INST126
import random

# Citation here for zork!!
print("Welcome to The adventure of the great NBA player!")
statline = {"Points": 0, "Assists": 0, "Rebounds": 0, "Steals": 0, "Turnovers": 0,
            "Blocks": 0}  # This is the dictionary that will be used to keep track of season stats
username = str(input("What is your name?: ")).title()  # input line for users name that stays throughout the game
number = int(input("What number would you like to be?: "))
teams = ['Wizards', 'Hornets', 'Pelicans', 'Warriors', 'Heat', 'Sixers', 'Celtics', 'Spurs', 'Cavs', 'Rockets',
         'Raptors', 'Lakers', 'Clippers', 'Timberwolves', 'Suns', 'Kings', 'Knicks', 'Nets', 'Jazz', 'Bulls', 'Pacers',
         'Pistions', 'Bucks', 'Magic', 'Hawks', 'Mavs', "Blazers", 'Thunder', 'Pelicans', 'Grizzlies'] #List of teams that the user may choose from.
position = ['Point Guard', 'Shooting Guard', 'Small Forward', 'Power Forward', 'Center'] #List of positions the user may choose from
print(teams)

valid_Team = True
while valid_Team:
    what_team = input("What team would you like to play for?: ").title()
    for team in teams:
        if what_team == team:
            valid_Team = False
            break

print(position)

valid_position = True
while valid_position:
    what_position = input("What position would you like play?: ").title()
    for role in position:
        if what_position == role:
            valid_position = False
            break

print("Welcome to the NBA", username, "you are a", what_position, "who plays for the", what_team,
      " this is your rookie season, be prepared.")
print("This adventure will last 20 games! When prompted, enter 'quit' to exit after a game. Are you ready to play?")

loop = 1
while loop == 1:

    print("It is your first NBA game!")
    print("---------------------------------------------------------")
    print(
        "Coach decided to start you because they need you. You are the best player on the team. Coach believes in you! Get out there and play!")
    print("You have three options on how to approach them game. Either 'offensive', 'defensive', or play 'all around' ")
    First_game = input("How would you like to approach it?: ").title()
    # This block of code will serve as the basis for the rest of the program
    if First_game == "Offensive":  # If user chooses offensice then this block of code will be excecuted
        points = random.randint(12, 44)  # Randomize points within 12,44
        statline['Points'] += points  # Add value to dictionary with key the key "Points"
        rebounds = random.randint(1, 7)# Randomize rebounds between 1,7
        statline['Rebounds'] += rebounds # Add value to dictionary with key the key "Points"
        assists = random.randint(1, 5) # Randomize assists between 1,5
        statline['Assists'] += assists # Add value to dictionary with key the key "Points"
        steals = random.randint(0, 2) #Randomize steals between 0,2
        statline['Steals'] += steals # Add value to dictionary with key the key "Points"
        blocks = random.randint(0, 2) #Randomize blocks between 0,2
        statline['Blocks'] += blocks # Add value to dictionary with key the key "Points"
        turnovers = random.randint(0, 4) #Randommize turnovers between 1,2
        statline['Turnovers'] += turnovers # Add value to dictionary with key the key "Points"
        print("You had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
            points, rebounds, assists, steals, blocks,
            turnovers))  # Using this print statement to keep track of each performance
        loop = 2  # Will move code along to the next stage of the game, Game 2
    if First_game == "Defensive":#If user chooses defensive, this loop will be excecuted. 
        points = random.randint(5, 12)
        statline['Points'] += points
        rebounds = random.randint(5, 15)
        statline['Rebounds'] += rebounds
        assists = random.randint(1, 5)
        statline['Assists'] += assists
        steals = random.randint(5, 10)
        statline['Steals'] += steals
        blocks = random.randint(4, 6)
        statline['Blocks'] += blocks
        turnovers = random.randint(0, 4)
        statline['Turnovers'] += turnovers
        print("You had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
            points, rebounds, assists, steals, blocks, turnovers))
        loop = 2
    if First_game == "All Around":
        points = random.randint(5, 25)
        statline['Points'] += points
        rebounds = random.randint(5, 10)
        statline['Rebounds'] += rebounds
        assists = random.randint(5, 10)
        statline['Assists'] += assists
        steals = random.randint(3, 6)
        statline['Steals'] += steals
        blocks = random.randint(3, 8)
        statline['Blocks'] += blocks
        turnovers = random.randint(0, 3)
        statline['Turnovers'] += turnovers
        print("You had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
            points, rebounds, assists, steals, blocks, turnovers))
        loop = 2

    while loop == 2:
        if loop == 2:
            print("It is your 10th NBA game!(2nd game)")
            print("---------------------------------------------------------")
            choice = input(
                "Do you want to 'practice' before the game with Kobe Bryant or do you want go 'party' with friends from college? ").title()

        if choice == "Practice": #User given a choice and will then be led in a similar loop as the first one
            print("Kobe Bryant says that you should drop at least 30 points!")
            print(
                "It's game time. You feel good. You have three options on how to approach them game. Either 'offensive', 'defensive', or play 'all around'")
            Second_game = input("How would you like to approach it?: ").title()
            if Second_game == "Offensive":
                points = random.randint(30, 45)
                statline['Points'] += points
                rebounds = random.randint(10, 20)
                statline['Rebounds'] += rebounds
                assists = random.randint(5, 10)
                statline['Assists'] += assists
                steals = random.randint(5, 10)
                statline['Steals'] += steals
                blocks = random.randint(5, 8)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 2)
                statline['Turnovers'] += turnovers
                print(
                    "You had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your second game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 3 # Will take player to loop 3.
            if Second_game == "Defensive":
                points = random.randint(7, 21)
                statline['Points'] += points
                rebounds = random.randint(5, 15)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(5, 10)
                statline['Steals'] += steals
                blocks = random.randint(4, 6)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 3
            if Second_game == "All Around":
                points = random.randint(12, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 3
        elif choice == "Party": #Second option for loop 2. 
            print("You have a mean hangover and it will affect your performance.")
            print(
                "It's game time. You feel dizzy. You have three options on how to approach them game. Either 'offensive', 'defensive', or play 'all around'")
            Second_game = input("How would you like to approach it?: ").title()
            if Second_game == "Offensive":
                points = random.randint(10, 34)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 3
            if Second_game == "Defensive":
                points = random.randint(0, 15)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 3
            if Second_game == "All Around":
                points = random.randint(12, 19)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 3

    # GAME 24 BEGINS
    while loop == 3:
        if loop == 3:
            print("It is your 24th NBA game! (3rd game)")
            print("---------------------------------------------------------")
            print("Do you want to 'practice' before the game with Chris Paul or play 'Fortnite' before the game? ")
            choice = input("How would you like to approach it?: ").title()
        if choice == "Practice":
            print("Chris Paul said during practice that you are a bucket!")
            print(
                "You are hype for the game because your team is going to play against the best team in the western confernece. You have three options on how to approach them game. Either offensive, defensive, or play all around")
            Third_game = input("How would you like to approach it?: ").title()
            if Third_game == "Offensive":
                points = random.randint(12, 45)
                statline['Points'] += points
                rebounds = random.randint(10, 20)
                statline['Rebounds'] += rebounds
                assists = random.randint(7, 18)
                statline['Assists'] += assists
                steals = random.randint(5, 10)
                statline['Steals'] += steals
                blocks = random.randint(5, 8)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 2)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your second game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 4
            if Third_game == "Defensive":
                points = random.randint(12, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 4
            if Third_game == "All Around":
                points = random.randint(12, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 4
        elif choice == "Fortnite":
            print("You have played all night and you are extremely tired. Because of this, it will affect your game...")
            Third_game = input(
                "How do you want to approch the upcoming game? Either 'offensive','defensive' or 'all around' ").title()
            # PASTE HERE
            if Third_game == "Offensive":
                points = random.randint(10, 34)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 4
            if Third_game == "Defensive":
                points = random.randint(0, 15)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 4
            if Third_game == "All Around":
                points = random.randint(12, 19)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 4

    while loop == 4:
        if loop == 4:
            print("It is your 32nd NBA game! (4th game)")
            print("---------------------------------------------------------")
            choice = input(
                "A hot girl just asked you out on a date the night before the big game. Do you want to 'go out' or 'practice' with Coach? ").title()

        if choice == "Practice":
            print("Coach said you about to get more minutes! ")
            print(
                "You are hype for the game because you are about to get more minutes! How you wanna play tonight? Either offensive, defensive, or play all around? ")
            Fourth_game = input("How would you like to approach it?: ").title()
            if Fourth_game == "Offensive":
                points = random.randint(30, 45)
                statline['Points'] += points
                rebounds = random.randint(10, 20)
                statline['Rebounds'] += rebounds
                assists = random.randint(5, 10)
                statline['Assists'] += assists
                steals = random.randint(5, 10)
                statline['Steals'] += steals
                blocks = random.randint(5, 8)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 2)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your second game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 5
            if Fourth_game == "Defensive":
                points = random.randint(12, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 5
            if Fourth_game == "All Around":
                points = random.randint(12, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 5
        elif choice == "Go Out":
            print(
                "The date did not go so well and the girl never hit you up ever again. You took a mean L. Because of this, you are sad and will affect your game...")
            Fourth_game = input(
                "How would you like to approach the upcoming game after being shot down by a girl even though your an NBA player. Either 'offensive','defensive' or 'all around'?: ").title()
            if Fourth_game == "Offensive":
                points = random.randint(10, 34)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 5
            if Fourth_game == "Defensive":
                points = random.randint(0, 15)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 5
            if Fourth_game == "All Around":
                points = random.randint(12, 19)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 5
    while loop == 5:
        if loop == 5:

            print("It is your 46th NBA game! (5th game)")
            print("---------------------------------------------------------")
            choice = input(
                "Mom asked you to come home for the weekend. It has been awhile, do you want 'go home' or 'practice'? ").title()

        if choice == "Practice":
            print("Practicing did not positively or negatively affect your game ")
            print(
                "You are just chilling because you are going against the worst team in the NBA. How you wanna play tonight? Either offensive, defensive, or play all around? ")
            Fifth_game = input("How would you like to approach it?: ").title()
            if Fifth_game == "Offensive":
                points = random.randint(30, 45)
                statline['Points'] += points
                rebounds = random.randint(10, 20)
                statline['Rebounds'] += rebounds
                assists = random.randint(5, 10)
                statline['Assists'] += assists
                steals = random.randint(5, 10)
                statline['Steals'] += steals
                blocks = random.randint(5, 8)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 2)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your second game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 6
            if Fifth_game == "Defensive":
                points = random.randint(12, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 6
            if Fifth_game == "All Around":
                points = random.randint(12, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 6
        elif choice == "Go Home":
            print("Mom gave you courage and home food for the game. You feel like a BEAST!!")
            Fifth_game = input(
                "How would you like to approach the upcoming game after eating a home cooked meal? Either 'offensive', 'defensive' or 'all around' : ").title()
            if Fifth_game == "Offensive":
                points = random.randint(10, 34)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 6
            if Fifth_game == "Defensive":
                points = random.randint(0, 15)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 6
            if Fifth_game == "All Around":
                points = random.randint(12, 19)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 6

                # STOPPED HERE 5/15

    while loop == 6:
        if loop == 6:

            print("It is your 60th NBA game! (6th game)")
            print("---------------------------------------------------------")
            choice = input(
                "Your boys want to hang out with you. Do you want to 'chill' with them or 'practice'? ").title()
        if choice == "Practice":
            print("Practicing did not positively or negatively affect your game ")
            print(
                 "You are just chilling because you are going against the worst team in the NBA. How you wanna play tonight? Either offensive, defensive, or play all around? ")
            Sixth_game = input("How would you like to approach it?: ").title()
            if Sixth_game == "Offensive":
                points = random.randint(30, 45)
                statline['Points'] += points
                rebounds = random.randint(10, 20)
                statline['Rebounds'] += rebounds
                assists = random.randint(5, 10)
                statline['Assists'] += assists
                steals = random.randint(5, 10)
                statline['Steals'] += steals
                blocks = random.randint(5, 8)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 2)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your second game!" % (
                    points, rebounds, assists, steals, blocks, turnovers))
                loop = 7
            if Sixth_game == "Defensive":
                points = random.randint(12, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                    points, rebounds, assists, steals, blocks, turnovers))
                loop = 7
            if Sixth_game == "All Around":
                points = random.randint(12, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                    points, rebounds, assists, steals, blocks, turnovers))
                loop = 7
        elif choice == "Chill":
            print(
                "Your friends gave you courage and the strength to play well. You can play either offensive, defensive, or play all around?")

            Sixth_game = input("How would you like to approach it?: ").title()
            if Sixth_game == "Offensive":
                points = random.randint(10, 34)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 7
            if Sixth_game == "Defensive":
                points = random.randint(0, 15)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 7
            if Sixth_game == "All Around":
                points = random.randint(12, 19)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 7

    while loop == 7:
        if loop == 7:

            print("It is your 82nd NBA game! (Final game)")
            print("---------------------------------------------------------")
            choice = input(
                   "Since today is the last regular season game, do you want to 'sleep' the entire day or 'practice'? ").title()
            if choice == "Practice":
                print("Since this is your last game and you've practiced, you are going to dominate ")
                print(
                    "Last game man. How you wanna play tonight? Either offensive, defensive, or play all around? ")
            Final_game = input("How would you like to approach it?: ").title()
            if Final_game == "offensive":
                points = random.randint(35, 45)
                statline['Points'] += points
                rebounds = random.randint(15, 20)
                statline['Rebounds'] += rebounds
                assists = random.randint(7, 10)
                statline['Assists'] += assists
                steals = random.randint(7, 10)
                statline['Steals'] += steals
                blocks = random.randint(6, 8)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 2)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your second game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 8
            if Final_game == "Defensive":
                points = random.randint(15, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 8)
                statline['Assists'] += assists
                steals = random.randint(0, 8)
                statline['Steals'] += steals
                blocks = random.randint(0, 7)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 8
            if Final_game == "All Around":
                points = random.randint(20, 44)
                statline['Points'] += points
                rebounds = random.randint(1, 10)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 10)
                statline['Assists'] += assists
                steals = random.randint(0, 12)
                statline['Steals'] += steals
                blocks = random.randint(0, 10)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 8

        elif choice == "Sleep":
            print("Sleeping made you rejuvenated. You are going to do well. Have fun!")
            Final_game = input(
                "Last game man. How you wanna play tonight? Either offensive, defensive, or play all around?: ").title()
            if Final_game == "Offensive":
                points = random.randint(13, 34)
                statline['Points'] += points
                rebounds = random.randint(3, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(3, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 5)
                statline['Steals'] += steals
                blocks = random.randint(0, 6)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 4)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 8
            if Final_game == "Defensive":
                points = random.randint(10, 20)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                        points, rebounds, assists, steals, blocks, turnovers))
                loop = 8
            if Final_game == "All Around":
                points = random.randint(12, 19)
                statline['Points'] += points
                rebounds = random.randint(1, 7)
                statline['Rebounds'] += rebounds
                assists = random.randint(1, 5)
                statline['Assists'] += assists
                steals = random.randint(0, 2)
                statline['Steals'] += steals
                blocks = random.randint(0, 2)
                statline['Blocks'] += blocks
                turnovers = random.randint(0, 7)
                statline['Turnovers'] += turnovers
                print(
                    "you had %d points, %d rebounds, %d assists, %d steals, %d blocks, %d turnovers in your first game!" % (
                    points, rebounds, assists, steals, blocks, turnovers))
                loop = 8

        while loop == 8:
            if loop == 8:
                print("You made it to the end of your first NBA season! Congrats on completing your rookie year.")
                choice = input("Now that your season is over, you can 'retire' or 'play again': ")
                if choice == 'retire':
                    print(
                        "You retired after 1 season in the NBA. Sadly you couldn't keep them checks coming, but atleast you have the memories and can tell people you played in the leauge.")
                    break
                if choice == 'play again':
                    loop = 1






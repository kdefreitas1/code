
import random
import time

turn = 0 # counts num of turns
total_score = 0 # counts total score for player
cpu_total = 0 # counts computer total
round_score = 0 # counts round score
cpu_speed = 0.75 # changes speed for computer default is .75
cpu_difficulty, cpu_num = "easy", 15 # changes difficulty for computer default is easiest
"""

for all inputs capitalization does not matter

"""
# function to ask for roll or bank
def choose():
    return input("Would you like to roll or bank? ")

print("Welcome to the Game of Pig!")
play_choice = input("Would you like to Play or go to Settings? ")
"""
while true so user get reprompted the questions
will break after user chooses speed and difficulty
will break if they choose to play
"""

while True:
    # everything in here is for changing settings of game
    if play_choice.lower() == "settings":
        print()
        #speed choice for computer
        print("What speed do you want the computer?")
        speed_choice = input("Normal, Fast, or Instant: ")
        if speed_choice.lower() == "fast":
            cpu_speed = 0.5
        elif speed_choice.lower() == "instant":
            cpu_speed = 0
        elif speed_choice.lower() == "normal":
            pass
        else:
            print()
            print("That is not a option.")
            print("Please only type 'Normal' 'Fast' 'Instant'")
            continue
        print()
        """
        while true needed to repromt question
        every difficulty choice will break out of loop
        """
        while True:
            print("What difficulty do you want the computer?")
            difficulty_choice = input("Easy, Normal, Hard, or Difficult: ")
            
            if difficulty_choice.lower() == "normal":
                cpu_difficulty, cpu_num = "normal", 20
                break
            elif difficulty_choice.lower() == "hard":
                cpu_difficulty, cpu_num = "hard", 25
                break
            elif difficulty_choice.lower() == "easy":
                break
            elif difficulty_choice.lower() == "difficult":
                cpu_difficulty = "difficult"
                break
            else:#this is if one of the difficulties is not typed
                print()
                print("That is not a option.")
                print("Please only type 'Easy' 'Normal' 'Hard' 'Difficult'")
                print()
                continue
    elif play_choice.lower() == "play": 
        print()
        break
    else: #incase anything but play and settings is typed
        print()
        print("That is not a option.")
        print("Please only type 'Play' or 'Settings'")
        print()
        play_choice = input("Would you like to Play or go to Settings? ")
        continue
    print()
    break
"""
everything in this code is for the game

while loop repeats all code till 100 or more score
"""
while True:
    turn += 1
    print("Turn " + str(turn))
    print("Your Total Score is: " + str(total_score))
    print("Computer Total Score is: " + str(cpu_total))
    print("This round you have : " + str(round_score))
    choice = choose() #assign choose function to variable
    print()
    """
    everything in this while loop is for user
    
    repeats till bank or roll 1
    """
    while True:
        # this is for when you roll
        if choice.lower() == "roll":
            roll = random.randint(1,6) # random num for dice roll
            round_score += roll  
            # this is when you roll a 1
            if roll == 1:
                round_score = 0
                print("You rolled a 1!")
                print("You get a zero for this round!")
                print()
                break
            print("You rolled a " + str(roll) + ".")
            print("This round you have: " + str(round_score))
            choice = choose()
            print()
        # this is for when you choose to bank
        elif choice.lower() == "bank":
            total_score += round_score
            round_score = 0
            break
        # this is if you dont type roll or bank
        else: 
            print("Please only type roll or bank.")
            choice = choose()
            print()
            continue
    # this is when you win the game (when score is 100 or more)
    if total_score >= 100:
        print("Congratulations! You won on " + str(turn) + " turns!")
        break
    """
    everything in this while loop is for the computer 
    
    while loop repeats till a 1 or when the computer is needed to bank
    """
    while True:
        roll = random.randint(1,6) # random num for dice roll
        round_score += roll
        # for making computer type slower
        time.sleep(cpu_speed)
        cpu_list = ["The computer rolled a 1. End of turn.", "The computer rolled a " + str(roll) + ".",
        "This round the computer has: " + str(round_score),"The computer has not chosen to roll again.",
        "The computer chooses to roll again."] 
        # if computer gets a one
        if roll == 1:
            round_score = 0
            print(cpu_list[0])#computer rolled a 1
            print()
            time.sleep(cpu_speed)
            break
        print(cpu_list[1])#computer rolled _
        print(cpu_list[2])#this round computer has _
        """
        cpu_list 3 is computer has not chosen to roll again
        cpu_list 4 is computer has chosen to roll again
        
        if statements are for difficulties
        all else statements is the computer chooses to roll again and continues to top 
        """
        # computer rolls till more than difficulty number (15, 20, or 25)
        if cpu_difficulty != "difficult":
            if round_score > cpu_num:
                cpu_total += round_score
                round_score = 0
                print(cpu_list[3])
                print()
                time.sleep(cpu_speed)
                break
            else:
                print(cpu_list[4])
                print()
                roll = 0
                continue
        elif cpu_difficulty == "difficult":
            """
            everything the computer does is based of the end race or keep pace strategy 
            the computer checks for these things - 
            If either player has a score of 71 or higher, roll to win. 
            Otherwise, hold on 21 plus the difference between scores divided by 8.
            """
            if total_score < 71 and cpu_total < 71:
                divide_total = round((cpu_total - total_score) / 8)
                abs(divide_total)
                if round_score > 21+divide_total:
                    cpu_total += round_score
                    round_score = 0
                    print(cpu_list[3])
                    print()
                    time.sleep(cpu_speed)
                    break
                else:
                    print(cpu_list[4])
                    print()
                    roll = 0
            elif total_score >= 71 or cpu_total >= 71:#if any total is over 71 computer rolls to win
                check = round_score + cpu_total # for checking if score is 100 or more so computer will bank when needed
                if check >= 100:
                    cpu_total += round_score
                    round_score = 0
                    print(cpu_list[3])
                    print()
                    time.sleep(cpu_speed)
                    break
                else:
                    print(cpu_list[4])
                    print()
                    roll = 0
    # this is when cpu wins game
    if cpu_total >= 100:
        print("Good try! The computer won on " + str(turn) + " turns.")
        break
    

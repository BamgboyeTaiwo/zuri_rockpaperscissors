import random


def RP():
    ''' 
    Hello User

    Pick
    R for rock
    P for paper 

    S for Scissors
    '''

    User_Input = input("Enter a choice (R, P, S): ")
    possible_actions = ["R", "P", "S"]
    computer_pick = random.choice(possible_actions)

    if User_Input.capitalize() in possible_actions:
        User_Input = User_Input.capitalize()
        computer_pick = computer_pick.capitalize()
        
        print('true')
   

        print("Player(", User_Input, ")", ":", "CPU(", computer_pick, ")")

        if User_Input == computer_pick:
            # print(f"Both players selected {User_Input}. It's a tie!")
            print("Both players selected:", User_Input, "The game is a tie")
            print("Restarting program......")
            RP()
            
        elif User_Input == "R":
            if computer_pick == "S":
                print("R beats S! You win!")
            else:
                print("P beats R! You lose.")
        elif User_Input == "P":
            if computer_pick == "R":
                print("P beats R! You win!")
            else:
                print("S beats P! You lose.")
        elif User_Input == "S":
            if computer_pick == "P":
                print("S beats P! You win!")
            else:
                print("R beats S! You lose.")

    else:
        print("user input not is unknown")
        return


RP()
# importing random module for PC choice
import random as rd


# function for continue choice in the loop
def cont_choice():
    get_cont_choice = \
        input("Do you want to continue playing? 'y' or 'n'\n>> ").lower()
    return get_cont_choice


# function to reset score after final result
def reset_score():
    score["Game"] = 0
    score["PC"] = 0
    score["Player"] = 0


# Choice list using matrix
mtrx_swg_list = [[0, 2, 1],
                 [1, 0, 2],
                 [2, 1, 0]]
score = {"Player": 0, "PC": 0, "Game": 0}  # Score
swg_list = ["Snake", "Water", "Gun"]  # List to print
get_userName = input("Enter your name:\n>> ")  # getting username
# loop
while True:
    # random number for PC choice
    pc_choice = rd.randint(0, 2)
    # getting users choice
    get_usr_value = int(input("Choose a value to continue this game:\n\
    1. Snake\n\
    2. Water\n\
    3. Gun\n\
>> "))
    # minus 1 to match it with pc choice
    get_usr_choice = get_usr_value - 1
    # verifying if the value is valid or not
    if get_usr_choice not in mtrx_swg_list[0]:
        print("Invalid Choice. Please choose again.")
        continue
    usr_swg_choice = swg_list[get_usr_choice]  # choice Snake/Water/Gun
    pc_swg_choice = swg_list[pc_choice]  # choice Snake/Water/Gun
    pc_row_list = mtrx_swg_list[pc_choice]  # getting row from matrix list
    usr_clmn_value = pc_row_list[get_usr_choice]  # single value from row
    if usr_clmn_value == 0:  # verifying if its draw
        print(f"{usr_swg_choice} VS {pc_swg_choice}\nThis is a draw.")
        score["Game"] += 1  # updating number of game
        print(f"{get_userName}: {score['Player']} | PC Score: {score['PC']} | \
Total Game: {score['Game']}")
    elif usr_clmn_value == 1:  # verifying if its a win
        print(f"{usr_swg_choice} VS {pc_swg_choice}\nYou Win!!")
        score["Player"] += 1  # updating player score
        score["Game"] += 1
        print(f"{get_userName}: {score['Player']} | PC Score: {score['PC']} | \
Total Game: {score['Game']}")
    elif usr_clmn_value == 2:  # verifying if its a lose
        print(f"{usr_swg_choice} VS {pc_swg_choice}\nYou Lose!!")
        score["PC"] += 1
        score["Game"] += 1
        print(f"{get_userName}: {score['Player']} | PC Score: {score['PC']} | \
Total Game: {score['Game']}")
# using if else conditions for final results
    if score["Game"] == 10:  # verifying if user played 10 times
        print("\nFinal Result:\n")
        if score["Player"] > score["PC"]:  # verifying if you win the game
            print(f"Congratulations, {get_userName}!! You've won the final \
game.\nYour Final Score is: {score['Player']}\nPC Score: {score['PC']}")
            reset_score()  # resetting score
            if cont_choice() == 'n':  # choice to quit the game
                break
        elif score["Player"] == score["PC"]:  # verifying if its a draw game
            print(f"You tried your best but this is a draw.\nYour Final \
Score is: {score['Player']}\nPC Score: {score['PC']}")
            reset_score()
            if cont_choice() == 'n':
                break
        else:  # otherwise its a lose
            print(f"You Lose, {get_userName}.\nYour Final \
Score is: {score['Player']}\nPC Score: {score['PC']}")
            reset_score()
            if cont_choice() == 'n':
                break

# Incorporate the random library
import random

def computerWin():
    print("Computer win")

def userWin():
    print("User win")

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# reMatch check Conditionals
reMatch = "y"

# Run Conditionals
while( reMatch == "y" or reMatch == "Y"):
    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    if ((user_choice ==  "r") or (user_choice == "p") or (user_choice == "s")):
        print("Sorry wrong input data")
    if (user_choice == "r") and (computer_choice == "s"):
        userWin()
    elif (user_choice == "s") and (computer_choice == "r"):
        computerWin()
    elif (user_choice == "s") and (computer_choice == "p"):
        userWin()
    elif (user_choice == "p") and (computer_choice == "s"):
        computerWin()
    elif (user_choice == "p") and (computer_choice == "r"):
        userWin()
    elif (user_choice == "r") and (computer_choice == "p"):
        computerWin()
    else :
        print(f"System error : {user_choice} and {computer_choice}")
    # continue again
    reMatch = input("Lets play again [y/n]")



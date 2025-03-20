import random  # Importing the random module to make the computer's choice random

###################################

choices = ["rock", "paper", "scissors"]  # List of valid choices for the game
stage.set_background_color("HotPink")  # Set the background color of the stage to HotPink

#
# Creating two sprites: one for the computer and one for the user
computer = codesters.Sprite("dracula", -150, 0)  # Computer sprite placed on the left
user = codesters.Sprite("ghost", 150, 0)  # User sprite placed on the right

####################################

#
# Asking the user to choose between rock, paper, or scissors
user_choice = user.ask("Please enter rock, paper, scissors")

# Looping until the user enters a valid choice
while user_choice not in choices:  
    # If the user enters something other than rock, paper, or scissors, prompt again
    user_choice = user.ask("You did not enter rock, paper, scissors. Please re-enter")
    
# Once a valid choice is made, load the corresponding image for the user’s choice
user.load_image(user_choice)

#####################################
# Computer's choice is random, so we need to simulate that.

for i in range(random.randint(10, 25)):  
    # Random loop to make the computer's sprite change its image between 10 to 25 times
    comp_choice = random.choice(choices)  # Randomly select a choice for the computer (rock, paper, or scissors)
    computer.load_image(comp_choice)  # Load the corresponding image for the computer's choice

# Create a text object to display the winner (or tie) on the screen
winner = codesters.Text("", 0, 150)

############################################
# Game logic: Using conditional statements to determine the winner

#
if user_choice == comp_choice:
    # If both choices are the same, it’s a tie
    winner.set_text("Tie")
    
elif user_choice == "rock":
    # If user chose rock, check the computer's choice
    if comp_choice == "paper":
        winner.set_text("Computer Wins")  # Paper beats rock
    else:
        winner.set_text("End User Wins!")  # Rock beats scissors

elif user_choice == "paper":
    # If user chose paper, check the computer's choice
    if comp_choice == "scissors":
        winner.set_text("Computer Wins!")  # Scissors beats paper
    else:
        winner.set_text("End User Wins")  # Paper beats rock

else:
    # If user chose scissors, check the computer's choice
    if comp_choice == "rock":
        winner.set_text("Computer Wins!")  # Rock beats scissors
    else:
        winner.set_text("Scissors Beats Paper End User Wins")  # Scissors beats paper
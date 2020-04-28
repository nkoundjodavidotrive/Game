
import random


def intro():
    print("WELCOME TO AFRICA 🌍")
    player_name = input("\nPlease enter a player name: ").capitalize()

    print(f"""\nHello {player_name}😊\nLets see how well do you know countries that constitute Africa 🤔🤔🤔

GAME RULES
1) A dice will be rolled once, and consequently you must type the name of an african country starting with the letter of the output gotten from the dice.
2) You have a maximum number of 2 trials after which you loose, if you could not correctly type in a country name in conformity with Rule1.

                        Accuracy in Brainstorming will be the key to your success. Goodluck!
            """)


def playing():

    maximum_number_of_trials = 2
    current_number_of_trials = 0

    possible_outputs_from_dice = ["a", "b", "c", "d", "e", "g", "k", "l", "m", "n", "r", "s", "t", "u", "z"]
    rolling_the_dice = random.choice(possible_outputs_from_dice)
    dice_outcome = f"Dice Outcome: {rolling_the_dice}"

    while current_number_of_trials < maximum_number_of_trials:
        print(dice_outcome)
        user_answer = input(f"Enter the name of an African country starting with {rolling_the_dice}: ").capitalize()
        current_number_of_trials += 1

        list_of_countries_in_africa = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
                                       "Cape Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
                                       "Congo", "Ivory Coast", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea",
                                       "Swaziland", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea",
                                       "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi",
                                       "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger",
                                       "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles",
                                       "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania",
                                       "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"]

        if user_answer in list_of_countries_in_africa:
            correct_answer = "correct answer 👍"
            print(correct_answer)
            break

    else:
        print("Game Over...")
        return True

    play_again = input(f"Play again? (yes/no)").capitalize()

    if play_again == "Yes":
        return False
    else:
        return True



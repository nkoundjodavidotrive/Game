import random


def intro():
    print("WELCOME TO AFRICA 🌍")
    player_name = input("\nPlease enter a player name: ").capitalize()

    print(f"""\nHello {player_name}😊\nHow well do you know countries that constitute Africa? 🤔🤔🤔

GAME RULES:
1) A dice will be rolled once. Consequently you must type the name of a country in africa starting with the letter of the output gotten from the dice
2) You have a maximum number of 2 Trials, after which you loose, if you could not correctly type in a country name according to Rule1.

                        Rapidity in Brainstorming will be the key to your success. Goodluck
""")


class RoundOne:

    def round_one(self):

        maximum_number_of_trials = 2
        current_number_of_trials = 0

        possible_outputs_from_dice = ["a", "b", "c", "d", "e", "g", "k", "l", "m", "n", "r", "s", "t", "u", "z"]
        rolling_the_dice = random.choice(possible_outputs_from_dice)
        dice_outcome = f"Dice Outcome: {rolling_the_dice}"


        while current_number_of_trials < maximum_number_of_trials:
            print(dice_outcome)
            user_answer = input(f"Enter an African country starting with {rolling_the_dice}: ").capitalize()
            current_number_of_trials += 1

            list_of_53_countries_in_africa = ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
                                       "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
                                       "Congo", "Cote d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea",
                                       "Eswatini (formerly Swaziland)", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea",
                                       "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi",
                                       "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia", "Niger",
                                       "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", "Seychelles", "Sierra Leone",
                                       "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia",
                                       "Uganda", "Zambia", "Zimbabwe"]

            if user_answer in list_of_53_countries_in_africa:
                correct_answer = "correct answer 👍"
                print(correct_answer)
                break

        else:
            print("Game Over...")
            return True
        
        nochmal = input(f"Play again? (y/n)").capitalize()
        
        if nochmal == "Y":
            return False
        else:
            return True

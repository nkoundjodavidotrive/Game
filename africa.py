from Welcome2Africa import RoundOne, intro

intro()

spiel_ende = False

while spiel_ende == False:
    spiel_ende = RoundOne().round_one()
else:
    print("Good bye!")


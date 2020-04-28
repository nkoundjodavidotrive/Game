from Welcome2Africa_GameSettings import intro, playing

intro()

end_game = False

while not end_game:
    end_game = playing()
else:
    print("Thanks for sharing this experience with us. Good bye!")

def ask_player_action() -> str:
    while True:
        get_from_user = input("Please enter H or S. To continue H to pass the turn to dealer S: ")
        if (len(get_from_user) == 1) and get_from_user in ("S", "H"):
            return get_from_user



ask_player_action()



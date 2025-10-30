import io_player

def calculate_hand_value(hand: list[dict]) -> int:
    hand_value = 0
    for i in hand:
        if i["rank"] in ("J", "K", "Q"):
            int_rank = 10
        elif i["rank"] == "A":
             int_rank = 1
        else:
            int_rank = int(i["rank"])
        hand_value += int_rank
    return hand_value

# print(calculate_hand_value(player['hand']))


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop(0))
    player["hand"].append(deck.pop(0))

    dealer["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    # print(player["hand"])
    # print(dealer["hand"])
    print("Starting hand values ​​of a player",calculate_hand_value(player["hand"]))
    print("Starting hand values ​​of a dealer",calculate_hand_value(dealer["hand"]))




def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        print(dealer["hand"])
        dealer["hand"].append(deck.pop(0))
        if calculate_hand_value(dealer["hand"]) > 21:
            break
        elif calculate_hand_value(dealer["hand"]) >= 17:
            break
    if calculate_hand_value(dealer["hand"]) > 21:
        print("The dealer is disqualified")
        return False
    else:
        return True


# print(dealer_play(deck, dealer))


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    while True:
        user_choice = io_player.ask_player_action()
        if user_choice == "H":
            player["hand"].append(deck.pop(0))
            if calculate_hand_value(player["hand"]) > 21:
                print("Your total is greater than 21. You are disqualified")
        if user_choice == "S":
            dealer_p = dealer_play(deck, dealer)
            if not dealer_p:
                value_player = player["hand"]
                value_dealer = dealer["hand"]
                if value_dealer > value_player:
                    print("dealer win")
                elif value_dealer < value_player:
                    print("dealer win")

                

            
















# {'suite': 'H', 'rank': '2'},
# {'suite': 'H', 'rank': '3'},
# {'suite': 'H', 'rank': '4'},
# {'suite': 'H', 'rank': '5'},
# {'suite': 'H', 'rank': '6'},
# {'suite': 'H', 'rank': '7'},
# {'suite': 'H', 'rank': '8'},
# {'suite': 'H', 'rank': '9'},
# {'suite': 'H', 'rank': '10'},
# {'suite': 'H', 'rank': 'J'},
# {'suite': 'H', 'rank': 'Q'},
# {'suite': 'H', 'rank': 'K'},
# {'suite': 'H', 'rank': 'A'},
# {'suite': 'C', 'rank': '2'}
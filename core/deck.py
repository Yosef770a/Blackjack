

def create_card(suite:str, rank:str) -> dict:
    dict_valus = {
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "10",
    "J": "J",
    "Q": "Q",
    "K": "K",
    "A": "A",
}
    card = {
        "suite": suite,
        "rank": dict_valus.get(rank) }
    return card

# print(create_card("J", "2"))

def build_standard_deck() -> list[dict]:
    cards_list = []
    possible_rank = list(range(2,11)) + ["J","Q","K","A"]
    # print(possible_rank)
    suites = ["H","C","D","S"]
    for suite in suites:
        for rank in possible_rank:
            card = create_card(suite, str(rank))
            print(card)
            cards_list.append(card)
    return cards_list

print(build_standard_deck())



def division_test(dividend: int, divisor: int):
    num = divmod(dividend, divisor)
    # print(num[0])
    # print(num[1])
    if num[1]:
        return False
    return True


# print(division_test(10, 5))
# print(division_test(7, 5))
# print(division_test(15, 5))


import random
def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for i in range(swaps):
        while True:
            index_i = random.randint(0, len(deck) - 1)
            index_j = random.randint(0, len(deck) - 1)
            # print(index_j)
            if (index_i != index_j):
                if (division_test(index_j, 5)):
                    break
                if (division_test(index_j, 3)):
                    break
                if (division_test(index_j, 2)):
                    break
                if (division_test(index_j, 7)):
                    break
        save_card = deck[index_j]
        deck[index_j] = deck[index_i]
        deck[index_i] = save_card


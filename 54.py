#!/usr/bin/python3


CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARD_SUITS = ['C', 'D', 'H', 'S']


def extract_hand_from_line(line, begin_i, end_i):
    return [
        (CARD_VALUES.index(line[i]) + 2, CARD_SUITS.index(line[i + 1]))
        for i in range(begin_i, end_i, 3)
    ]


def rank_hand(hand):
    values = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    # print(f"{values=}")

    ### Shortcuts
    is_straight = all([ (val - i == values[0]) for i, val in enumerate(values) ])
    is_flush = len(set(suits)) == 1
    occurrences = sorted([values.count(i) for i in values])
    # print(f"{occurrences=}")

    ### NOTE: Match highest rank first
    hand_rank = 0
    highest_cards = reversed(sorted(values.copy()))

    ### Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    if (set(values) == {10, 11, 12, 13, 14}) and is_flush:
        print("Royal Flush")
        hand_rank = 10

    ### Straight Flush: All cards are consecutive values of same suit.
    elif is_straight and is_flush:
        print("Straight Flush")
        hand_rank = 9

    ### Four of a Kind: Four cards of the same value.
    elif occurrences == [1, 4, 4, 4, 4]:
        print("Four of a Kind")
        hand_rank = 8

        ### NOTE: Prioritise value of the 4 matching cards
        highest_cards = sorted(set(values)) ### E.G: [6,9]

    ### Full House: Three of a kind and a pair.
    elif occurrences == [2, 2, 3, 3, 3]:
        print("Full House")
        hand_rank = 7

    ### Flush: All cards of the same suit.
    elif is_flush:
        print("Flush")
        hand_rank = 6

    ### Straight: All cards are consecutive values.
    elif is_straight:
        print("Straight")
        hand_rank = 5

    ### Three of a Kind: Three cards of the same value.
    elif occurrences == [1, 1, 3, 3, 3]:
        print("Three of a Kind")
        hand_rank = 4
        highest_cards = [] ### TODO: Order 3-of-a-kind, then others

    ### Two Pairs: Two different pairs.
    elif occurrences == [1, 2, 2, 2, 2]:
        print("Two Pairs")
        hand_rank = 3
        highest_cards = [] ### TODO: Order high pair, then low pair, then others

    ### One Pair: Two cards of the same value.
    elif occurrences == [1, 1, 1, 2, 2]:
        print("One Pair")
        hand_rank = 2
        highest_cards = [] ### TODO

    else:
        ### High Card: Highest value card.
        print("High Card")
        hand_rank = 1

    return {
        "hand_rank": hand_rank,
        "highest_cards": highest_cards,
    }


def main():
    # line = "8C TS KC 9H 4S 7D 2S 5D 3S AC"
    line = "8C TS KC 9H 4S 7D 2S 5D AD AC"
    print(f"{line=}")

    ### Extract hands from text
    hand_1 = extract_hand_from_line(line, 0, 14)
    hand_2 = extract_hand_from_line(line, 15, 28)
    # print(hand_1)
    # print(hand_2)


    ### Rank hands
    rank_hand(hand_1)
    rank_hand(hand_2)


if __name__ == "__main__":
    main()

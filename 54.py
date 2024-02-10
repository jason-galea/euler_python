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
    hand_rank = 1
    highest_cards = reversed(sorted(values.copy())) ### Default

    if (set(values) == {10, 11, 12, 13, 14}) and is_flush: ### Royal Flush
        print("Royal Flush")
        hand_rank = 10

    elif is_straight and is_flush: ### Straight Flush
        print("Straight Flush")
        hand_rank = 9

    elif occurrences == [1, 4, 4, 4, 4]: ### Four of a Kind:
        print("Four of a Kind")
        hand_rank = 8

        ### NOTE: Prioritise value of the 4 matching cards
        highest_cards = sorted(set(values)) ### E.G: [6,9]

    elif occurrences == [2, 2, 3, 3, 3]: ### Full House
        print("Full House")
        hand_rank = 7

    elif is_flush: ### Flush
        print("Flush")
        hand_rank = 6

    elif is_straight: ### Straight
        print("Straight")
        hand_rank = 5

    elif occurrences == [1, 1, 3, 3, 3]: ### Three of a Kind
        print("Three of a Kind")
        hand_rank = 4

        for i in values:
            if values.count(i) == 3:
                three_of_a_kind_val = i
                break

        highest_cards = (
            sorted(filter((three_of_a_kind_val).__eq__, values))
            + sorted(filter((three_of_a_kind_val).__ne__, values))
        )

    elif occurrences == [1, 2, 2, 2, 2]: ### Two Pairs
        print("Two Pairs")
        hand_rank = 3

        ### I hate this
        pair_values = [i for i in values if (values.count(i) == 2)]
        highest_cards = (
            sorted(pair_values)
            + [i for i in values if (i not in pair_values)] ### Unsorted because len() == 1
        )

    elif occurrences == [1, 1, 1, 2, 2]: ### One Pair
        print("One Pair")
        hand_rank = 2

        for i in values:
            if values.count(i) == 3:
                one_pair_val = i
                break

        highest_cards = (
            sorted(filter((one_pair_val).__eq__, values))
            + sorted(filter((one_pair_val).__ne__, values))
        )

    else: ### High Card
        print("High Card")

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

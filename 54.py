#!/usr/bin/python3


CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARD_SUITS = ['C', 'D', 'H', 'S']


def extract_hand_from_line(line, begin_i, end_i):
    return [
        (CARD_VALUES.index(line[i]) + 2, CARD_SUITS.index(line[i + 1]))
        for i in range(begin_i, end_i, 3)
    ]


def find_value_with_count(values, count):
    for i in values:
        if values.count(i) == count:
            return i


def rank_hand(hand):
    # values = [card[0] for card in hand]
    values = list(sorted([card[0] for card in hand]))
    suits = [card[1] for card in hand]
    # print(f"{values=}")

    ### Shortcuts
    # values_sorted = sorted(values)
    # is_straight = all([ (val - i == values_sorted[0]) for i, val in enumerate(values_sorted) ])
    is_straight = all([ (val - i == values[0]) for i, val in enumerate(values) ])
    is_flush = len(set(suits)) == 1
    occurrences = sorted([values.count(i) for i in values])

    ### Handle aces-low straights
    if set(values) == {14, 2, 3, 4, 5}:
        print("(ACES-LOW) ", end='')
        is_straight = True
        values = [1 if (i == 14) else i for i in values] ### Replace 14 with 1


    ### NOTE: Match highest rank first
    hand_rank = 1
    tiebreaker_cards = reversed(sorted(values.copy())) ### Default

    if (set(values) == {10, 11, 12, 13, 14}) and is_flush: ### Royal Flush
        print("Royal Flush")
        hand_rank = 10

    elif is_straight and is_flush: ### Straight Flush
        print("Straight Flush")
        hand_rank = 9

    elif occurrences == [1, 4, 4, 4, 4]: ### Four of a Kind:
        print("Four of a Kind")
        hand_rank = 8

        tiebreaker_cards = (
            [find_value_with_count(values, 4)]
            + [find_value_with_count(values, 1)] ### No need to sort a single value
        )

    elif occurrences == [2, 2, 3, 3, 3]: ### Full House
        print("Full House")
        hand_rank = 7

        tiebreaker_cards = (
            [find_value_with_count(values, 3)]
            + [find_value_with_count(values, 2)]
        )

    elif is_flush: ### Flush
        print("Flush")
        hand_rank = 6

    elif is_straight: ### Straight
        print("Straight")
        hand_rank = 5

    elif occurrences == [1, 1, 3, 3, 3]: ### Three of a Kind
        print("Three of a Kind")
        hand_rank = 4

        three_count_val = find_value_with_count(values, 3)
        tiebreaker_cards = (
            [three_count_val]
            + sorted([i for i in values if (i != three_count_val)])
        )

    elif occurrences == [1, 2, 2, 2, 2]: ### Two Pairs
        print("Two Pairs")
        hand_rank = 3

        high_pair_val = find_value_with_count(list(reversed(sorted(values))), 2)
        low_pair_val = find_value_with_count(list(sorted(values)), 2)
        tiebreaker_cards = [high_pair_val] + [low_pair_val] + [find_value_with_count(values, 1)]

    elif occurrences == [1, 1, 1, 2, 2]: ### One Pair
        print("One Pair")
        hand_rank = 2

        two_count_val = find_value_with_count(values, 2)
        tiebreaker_cards = (
            [two_count_val]
            + sorted([i for i in values if (i != two_count_val)])
        )

    else: ### High Card
        print("High Card")

    return hand_rank, list(tiebreaker_cards)


def main():
    result = [0, 0]

    with open("./54_poker.txt", "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    # for line in [ ### Example hands
    #     "5H 5C 6S 7S KD 2C 3S 8S 8D TD", ### Pairs
    #     "5D 8C 9S JS AC 2C 5C 7D 8S QH", ### High card
    #     "2D 9C AS AH AC 3D 6D 7D TD QD", ### 3-of-a-kind, Flush
    #     "4D 6S 9H QH QC 3D 6D 7H QD QS", ### Pair
    #     "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D", ### Full House
    # ]:
    # for line in ["2H 7D 4C 4D 4S 3C 3D 3S 2S 9D"]: ### 3-of-a-kind
    # for line in ["2H 3D 4C 5D 6S AC 2D 3S 4S 5D"]: ### Straights
    for line in lines:

        hand_1 = extract_hand_from_line(line, 0, 14)
        hand_2 = extract_hand_from_line(line, 15, 28)

        print(f"{line[:14]} -> ", end='')
        hand_1_rank, hand_1_spares = rank_hand(hand_1)
        print(f"{line[15:]} -> ", end='')
        hand_2_rank, hand_2_spares = rank_hand(hand_2)

        if hand_1_rank == hand_2_rank:
            for i in range(len(hand_1_spares)): # pylint: disable=consider-using-enumerate
                if hand_1_spares[i] != hand_2_spares[i]:
                    winner = 1 if (hand_1_spares[i] > hand_2_spares[i]) else 2
                    print(f"Hand {winner} wins!")
                    break
        else:
            winner = 1 if (hand_1_rank > hand_2_rank) else 2
            print(f"Hand {winner} wins!")

        result[winner - 1] += 1
        print()

    for i in [1, 2]:
        print(f"Player {i} won {result[i - 1]} hands")


if __name__ == "__main__":
    main()

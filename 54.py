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
            if values.count(i) == 2:
                one_pair_val = i
                break

        highest_cards = (
            sorted(filter((one_pair_val).__eq__, values))
            + sorted(filter((one_pair_val).__ne__, values))
        )

    else: ### High Card
        print("High Card")

    return hand_rank, list(highest_cards)


def main():
    with open("./54_poker.txt", "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    result = [0, 0]
    # max_lines = 3
    # current_lines = 1
    for line in lines:
        # if current_lines == max_lines:
        #     break

        # print(f"\n==> INFO: Round {current_lines}")

        ### Extract hands from text
        hand_1 = extract_hand_from_line(line, 0, 14)
        hand_2 = extract_hand_from_line(line, 15, 28)
        # print(hand_1)
        # print(hand_2)


        ### Rank hands
        # print(f"Hand 1: '{line[:14]}'")
        print(f"'{line[:14]}' -> ", end='')
        hand_1_rank, hand_1_spares = rank_hand(hand_1)

        # print(f"Hand 2: '{line[15:]}'")
        print(f"'{line[15:]}' -> ", end='')
        hand_2_rank, hand_2_spares = rank_hand(hand_2)


        ### Decide winner
        if hand_1_rank == hand_2_rank:
            # print(f"MATCHING RANKS!!!!!")

            for i in range(len(hand_1_spares)): # pylint: disable=consider-using-enumerate
                if hand_1_spares[i] != hand_2_spares[i]:
                    # print(f"{hand_1_spares[i]=}")
                    # print(f"{hand_2_spares[i]=}")

                    winner = 1 if (hand_1_spares[i] > hand_2_spares[i]) else 2
                    print(f"Hand {winner} wins!")
                    break

        else:
            winner = 1 if (hand_1_rank > hand_2_rank) else 2
            print(f"Hand {winner} wins!")

        result[winner - 1] += 1
        print()

    # print(f"Player 1 won {result['1']} hands")
    # print(f"Player 2 won {result['2']} hands")
    for i in [1,2]:
        print(f"Player {i} won {result[i - 1]} hands")


if __name__ == "__main__":
    main()

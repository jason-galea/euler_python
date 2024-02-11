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
    values = list(sorted([card[0] for card in hand])) ### Value order does NOT need to match suit order
    suits = [card[1] for card in hand]

    ### Shortcuts
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
    tiebreaker_cards = list(reversed(sorted(values.copy()))) ### Default

    if (set(values) == {10, 11, 12, 13, 14}) and is_flush: ### Royal Flush
        hand_rank = 10

    elif is_straight and is_flush: ### Straight Flush
        hand_rank = 9

    elif occurrences == [1, 4, 4, 4, 4]: ### Four of a Kind:
        hand_rank = 8
        tiebreaker_cards = (
            [find_value_with_count(values, 4)]
            + [find_value_with_count(values, 1)] ### No need to sort a single value
        )

    elif occurrences == [2, 2, 3, 3, 3]: ### Full House
        hand_rank = 7
        tiebreaker_cards = (
            [find_value_with_count(values, 3)]
            + [find_value_with_count(values, 2)]
        )

    elif is_flush: ### Flush
        hand_rank = 6

    elif is_straight: ### Straight
        hand_rank = 5

    elif occurrences == [1, 1, 3, 3, 3]: ### Three of a Kind
        hand_rank = 4
        three_count_val = find_value_with_count(values, 3)
        tiebreaker_cards = (
            [three_count_val]
            + list(reversed(sorted([i for i in values if (i != three_count_val)])))
        )

    elif occurrences == [1, 2, 2, 2, 2]: ### Two Pairs
        hand_rank = 3
        high_pair_val = find_value_with_count(list(reversed(sorted(values))), 2)
        low_pair_val = find_value_with_count(list(sorted(values)), 2)
        tiebreaker_cards = [high_pair_val] + [low_pair_val] + [find_value_with_count(values, 1)]

    elif occurrences == [1, 1, 1, 2, 2]: ### One Pair
        hand_rank = 2
        two_count_val = find_value_with_count(values, 2)
        tiebreaker_cards = (
            [two_count_val]
            + list(reversed(sorted([i for i in values if (i != two_count_val)])))
        )

    return hand_rank, list(tiebreaker_cards)


def main():
    player_1_wins = 0
    result = [0, 0]

    with open("./54_poker.txt", "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    for line in lines:

        hand_1 = extract_hand_from_line(line, 0, 14)
        hand_2 = extract_hand_from_line(line, 15, 28)

        hand_1_rank, hand_1_spares = rank_hand(hand_1)
        hand_2_rank, hand_2_spares = rank_hand(hand_2)

        if hand_1_rank == hand_2_rank:
            for i in range(len(hand_1_spares)): # pylint: disable=consider-using-enumerate
                if hand_1_spares[i] != hand_2_spares[i]:
                    winner = 1 if (hand_1_spares[i] > hand_2_spares[i]) else 2
                    break
                    # if (hand_1_spares[i] > hand_2_spares[i]):
                    #     winner = 1
                    #     break

        else:
            winner = 1 if (hand_1_rank > hand_2_rank) else 2
        # elif (hand_1_rank > hand_2_rank):
        #     pass


        result[winner - 1] += 1
        # print()

    for i in [1, 2]:
        print(f"Player {i} won {result[i - 1]} hands")


if __name__ == "__main__":
    main()

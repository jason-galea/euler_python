#!/usr/bin/python3


CARD_VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
CARD_RANKS = ['C', 'D', 'H', 'S']


def extract_hand_from_line(line, begin_i, end_i):
    return [
        (CARD_VALUES.index(line[i]) + 2, CARD_RANKS.index(line[i + 1]))
        for i in range(begin_i, end_i, 3)
    ]


def rank_hand(hand):

    ### Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    ### Straight Flush: All cards are consecutive values of same suit.
    ### Four of a Kind: Four cards of the same value.
    ### Full House: Three of a kind and a pair.
    ### Flush: All cards of the same suit.
    ### Straight: All cards are consecutive values.
    ### Three of a Kind: Three cards of the same value.
    ### Two Pairs: Two different pairs.
    ### One Pair: Two cards of the same value.
    ### High Card: Highest value card.

    ### Order remaining cards from highest to lowest

    return {
        "hand_rank": 0,
        "highest_cards": [3,2,1],
    }


def main():
    line = "8C TS KC 9H 4S 7D 2S 5D 3S AC"

    ### Extract hands from text
    hand_1 = extract_hand_from_line(line, 0, 14)
    hand_2 = extract_hand_from_line(line, 15, 28)
    print(hand_1)
    print(hand_2)


    ### Rank hands
    rank_hand(hand_1)


if __name__ == "__main__":
    main()

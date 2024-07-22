# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# In poker.txt, how many hands does Player 1 win?
from datetime import datetime

suits = {"S": 3, "H": 2, "C": 1, "D": 0}
values = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "J": 9,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
}


def sort_hand(hand):
    new_hand = [""] * 52
    for card in hand:
        value, suit = [*card]
        index = values[value] + (13 * suits[suit])
        new_hand[index] = card
    return [c for c in new_hand if c != ""]


def is_flush(hand):
    suit = hand[0][1]
    for card in hand:
        if not suit in card:
            return False
    return True


def is_straight(hand):
    vals = [values[c[0]] for c in hand]
    vals.sort()
    first_val = vals[0]
    next_val = first_val + 1
    for i in range(1, 5):
        if vals[i] != next_val:
            return False
        next_val += 1
    return True


def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)


def is_royal_flush(hand):
    return is_straight_flush(hand) and hand[0][0] == "T"


def find_num_values(hand):
    num_vals = {}
    for card in hand:
        val = card[0]
        num_vals[val] = num_vals.get(val, 0) + 1
    return num_vals


def is_pair_of_pairs(num_vals):
    # look for 2 2s
    count = 0
    for val in num_vals.values():
        if val == 2:
            count += 1
    if count == 2:
        return True
    return False


def find_winner_by_high_val(num_vals1, num_vals2):
    scores1 = [values[val] for val in num_vals1]
    scores2 = [values[val] for val in num_vals2]
    scores1.sort()
    scores2.sort()
    while scores1 and scores2:
        score1 = scores1.pop()
        score2 = scores2.pop()
        if score1 > score2:
            return 1
        if score2 > score1:
            return 2
    return 1


def evaluate_winner(hand1, hand2):
    if is_royal_flush(hand1):
        return hand1
    if is_royal_flush(hand2):
        return hand2
    num_vals1 = find_num_values(hand1)
    num_vals2 = find_num_values(hand2)
    winner_by_high_val = find_winner_by_high_val(num_vals1, num_vals2)
    if is_straight_flush(hand1):
        if is_straight_flush(hand2):
            print(f"comparing {hand1} vs {hand2} for straight flush")
            print(f"winner by high value is: {winner_by_high_val}")
            if winner_by_high_val == 1:
                return hand1
            return hand2
        return hand1
    if is_straight_flush(hand2):
        return hand2
    if 4 in num_vals1.values():
        if 4 in num_vals2.values():
            print(f"comparing {hand1} vs {hand2} for 4 of a kind")
            print(f"winner by high value is: {winner_by_high_val}")
            if winner_by_high_val == 1:
                return hand1
            return hand2
        return hand1
    if 4 in num_vals2.values():
        return hand2
    if 3 in num_vals1.values() and 2 in num_vals1.values():
        if 3 in num_vals2.values() and 2 in num_vals2.values():
            print(f"comparing {hand1} vs {hand2} for 3 of a kind and a pair")
            print(f"winner by high value is: {winner_by_high_val}")
            if winner_by_high_val == 1:
                return hand1
            return hand2
        return hand1
    if 3 in num_vals2.values() and 2 in num_vals2.values():
        return hand2
    if is_flush(hand1):
        if is_flush(hand2):
            print(f"comparing {hand1} vs {hand2} for flush")
            print(f"winner by high value is: {winner_by_high_val}")
            if winner_by_high_val == 1:
                return hand1
            return hand2
        return hand1
    if is_flush(hand2):
        return hand2
    if is_straight(hand1):
        if is_straight(hand2):
            print(f"comparing {hand1} vs {hand2} for straight")
            print(f"winner by high value is: {winner_by_high_val}")
            if winner_by_high_val == 1:
                return hand1
            return hand2
        return hand1
    if is_straight(hand2):
        return hand2
    if 3 in num_vals1.values():
        if 3 in num_vals2.values():
            print(f"comparing {hand1} vs {hand2} for 3 of a kind")
            print(f"winner by high value is: {winner_by_high_val}")
            if winner_by_high_val == 1:
                return hand1
            return hand2
        return hand1
    if 3 in num_vals2.values():
        return hand2
    if is_pair_of_pairs(num_vals1):
        if is_pair_of_pairs(num_vals2):
            print(f"comparing {hand1} vs {hand2} for pair of pairs")
            print(f"winner by high value is: {winner_by_high_val}")
            if winner_by_high_val == 1:
                return hand1
            return hand2
        return hand1
    if is_pair_of_pairs(num_vals2):
        return hand2
    if 2 in num_vals1.values():
        if 2 in num_vals2.values():
            print(f"comparing {hand1} vs {hand2} for 2 of a kind")
            print(f"winner by high value is: {winner_by_high_val}")
            val1 = [values[val] for val in num_vals1 if num_vals1[val] == 2][0]
            val2 = [values[val] for val in num_vals2 if num_vals2[val] == 2][0]
            if val1 > val2:
                return hand1
            if val2 > val1:
                return hand2
            if winner_by_high_val == 1:
                return hand1
            return hand2
        return hand1
    if 2 in num_vals2.values():
        return hand2
    if winner_by_high_val == 1:
        return hand1
    return hand2


print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

count = 0

with open("0054_poker.txt") as f:
    for line in f:
        # read in the line, separating to two hands
        cards = line.strip().split(" ")
        hand1 = sort_hand(cards[:5])
        hand2 = sort_hand(cards[5:])

        # evaluate winner of hands
        winning_hand = evaluate_winner(hand1, hand2)
        if winning_hand == hand1:
            # if player 1, add to count
            count += 1
    f.close()

print(count)
print(f"{datetime.now().strftime('%H:%M:%S.%f')}")

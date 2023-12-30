from collections import Counter

# From (5,) to (1, 1, 1, 1, 1); higher is better.
def hand_type(hand):
    return tuple(sorted(Counter(hand).values(), reverse=True))

def sort_key_part1(hand):
    card_values = tuple('23456789TJQKA'.index(card) for card in hand)
    return (hand_type(hand), card_values)

def sort_key_part2(hand):
    best_type = max(hand_type(hand.replace('J', card))
                    for card in 'AKQT98765432')
    card_values = tuple('J23456789TQKA'.index(card) for card in hand)
    return (best_type, card_values)

with open('input.in') as f:
    hands_bids = [(hand, int(bid))
                  for line in f
                  for hand, bid in (line.split(),)]

for part, sort_key in [(1, sort_key_part1), (2, sort_key_part2)]:
    hands_bids.sort(key=lambda entry: sort_key(entry[0]))
    answer = sum((i + 1) * bid for i, (_, bid) in enumerate(hands_bids))
    print(f"Part {part}: {answer}")

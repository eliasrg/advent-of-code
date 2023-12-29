from collections import Counter

# Lower is better
def hand_type(hand):
    counts = Counter(Counter(hand).values())

    return next(
        i for i, cond in enumerate([
            5 in counts, # Five of a kind
            4 in counts, # Four of a kind
            3 in counts and 2 in counts, # Full house
            3 in counts, # Three of a kind
            counts[2] == 2, # Two pair
            counts[2] == 1, # One pair
            True # High card
        ]) if cond)

def sort_key_part1(hand):
    card_values = tuple('AKQJT98765432'.index(card) for card in hand)
    return (hand_type(hand), card_values)

def sort_key_part2(hand):
    if hand == 'JJJJJ':
        best_type = 0 # Five of a kind
    else:
        [(best_card, _)] = Counter(hand.replace('J', '')).most_common(1)
        best_type = hand_type(hand.replace('J', best_card))
    card_values = tuple('AKQT98765432J'.index(card) for card in hand)
    return (best_type, card_values)

with open('input.in') as f:
    hands_bids = [(hand, int(bid))
                  for line in f
                  for hand, bid in (line.split(),)]

for part, sort_key in [(1, sort_key_part1), (2, sort_key_part2)]:
    hands_bids.sort(key=lambda entry: sort_key(entry[0]), reverse=True)
    answer = sum((i + 1) * bid for i, (_, bid) in enumerate(hands_bids))
    print(f"Part {part}: {answer}")

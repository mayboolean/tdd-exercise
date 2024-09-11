VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    
    score = 0
    ace_count = 0

    if not (2 <= len(hand) <= 5):
        return None
    
    for card in hand:
        if card in VALID_CARDS:
            if isinstance(card, int):
                score += card
            elif isinstance(card, str) and not card == "Ace":
                score += 10
            elif card == "Ace":
                ace_count += 1
            else:
                return None
        else:
            return None
            
    ace_value = 11
    for i in range(ace_count):
        if score + ace_value + (ace_count-1) > 21:
            ace_value = 1
        score += ace_value    
    
    if score > 21:
        return("Bust!")
    
    return score
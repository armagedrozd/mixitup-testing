# bj_common.py
import json
import os
import random
import sys

# Set the path to the game state file
# We assume that the scripts are all in the same folder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GAME_FILE = os.path.join(SCRIPT_DIR, 'bj_game.json')
WINNERS = os.path.join(SCRIPT_DIR, 'winners.txt')
LOSERS  = os.path.join(SCRIPT_DIR, 'losers.txt')

# --- Working with cards ---

def create_deck():
    """It shuffles a standard 52-card deck."""
    suits = ['♠️', '♥️', '♦️', '♣️']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_value(card):
    """Returns the value of the card used to calculate points."""
    if card['rank'] in ['J', 'Q', 'K']:
        return 10
    elif card['rank'] == 'A':
        return 11  # We return 11, but we’ll handle a special case for the ace
    else:
        return int(card['rank'])

def calculate_hand_value(hand):
    """Calculates the value of a hand, taking into account that an ace can be either 1 or 11."""
    value = 0
    aces = 0
    for card in hand:
        val = card_value(card)
        if val == 11:
            aces += 1
        value += val

    # If we have aces and our total is more than 21, we change the aces from 11 to 1
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

def card_to_string(card):
    """Converts a card into a string for display in the chat."""
    return f"{card['rank']}{card['suit']}"

def hand_to_string(hand):
    """Converts the hand into a string for output."""
    return ', '.join([card_to_string(card) for card in hand])

# --- Working with the state file ---

def load_game():
    """Loads the game state from a file. If the file does not exist, it returns None."""
    if os.path.exists(GAME_FILE):
        with open(GAME_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_game(game_state):
    """Saves the game state to a file."""
    with open(GAME_FILE, 'w', encoding='utf-8') as f:
        json.dump(game_state, f, ensure_ascii=False, indent=4)

def clear_game():
    """Deletes the game state file."""
    if os.path.exists(GAME_FILE):
        os.remove(GAME_FILE)

# --- Functions for displaying messages ---

def send_message(message):
    """Displays a message in the chat. Mix It Up captures scriptresult."""
    print(message)

def send_error(message):
    """Displays an error message."""
    print(f"[Ошибка] {message}")

def get_username():
    """Retrieves the username from an argument or from $username."""
    # In Mix It Up, we pass the username as an argument
    # This is done to ensure the script is versatile.
    # If no argument is passed, we attempt to use $targetusername
    # However, it is always best to pass $username as the first argument.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "Unknown"
    
def add_WINNERS_to_file(user_id: str) -> bool:
    """
    Adds an ID to the file. Returns True if it has been added, False if it already exists.
    """
    user_id = str(user_id).strip()  
    # Let’s check if it’s already there
    if os.path.exists(WINNERS):
        with open(WINNERS, "r", encoding="utf-8") as f:
            existing = {line.strip() for line in f}
        if user_id in existing:
            print(f"SKIP: {user_id} already exists")
            return False
    
    # Add
    with open(WINNERS, "a", encoding="utf-8") as f:
        f.write(user_id + "\n")
    return True

def add_LOSERS_to_file(user_id: str) -> bool:
    """
    Adds an ID to the file. Returns True if it has been added, False if it already exists.
    """
    user_id = str(user_id).strip()
        
    # Let’s check if it’s already there
    if os.path.exists(LOSERS):
        with open(LOSERS, "r", encoding="utf-8") as f:
            existing = {line.strip() for line in f}
        if user_id in existing:
            print(f"SKIP: {user_id} already exists")
            return False
    
    # Add
    with open(LOSERS, "a", encoding="utf-8") as f:
        f.write(user_id + "\n")
    return True

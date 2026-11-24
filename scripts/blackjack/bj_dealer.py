# -*- coding: utf-8 -*-
# bj_dealer.py
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, __file__.rsplit('\\', 1)[0] if '\\' in __file__ else __file__.rsplit('/', 1)[0])
from bj_common import *

def main():
    username = """$username"""
    game_state = load_game()

    if not game_state:
        send_message("Нет активной игры.")
        return

    # We check that the game is in the ‘waiting for the dealer’ state
    if game_state['status'] != 'waiting_for_dealer':
        return

    # Let’s play as the dealer
    dealer_hand = game_state['dealer_hand']
    dealer_value = calculate_hand_value(dealer_hand)

    # The dealer draws cards until their total is less than 17
    while dealer_value < 17:
        new_card = game_state['deck'].pop()
        dealer_hand.append(new_card)
        dealer_value = calculate_hand_value(dealer_hand)

    game_state['dealer_hand'] = dealer_hand
    dealer_hand_str = hand_to_string(dealer_hand)

    message = f"Дилер открывает карты: {dealer_hand_str} (Сумма: {dealer_value}).\n"

    # Announcing the winners
    results = []
    for player in game_state['players']:
        player_value = player['value']
        if player_value > 21:
            results.append(f"@{player['name']} — перебор, проиграл.")
            add_LOSERS_to_file(player['name'])
        elif dealer_value > 21:
            results.append(f"@{player['name']} — выиграл! (Дилер перебрал)")
            add_WINNERS_to_file(player['name'])
        elif player_value > dealer_value:
            results.append(f"@{player['name']} — выиграл!")
            add_WINNERS_to_file(player['name'])
        elif player_value < dealer_value:
            results.append(f"@{player['name']} — проиграл.")
            add_LOSERS_to_file(player['name'])
        else:
            results.append(f"@{player['name']} — ничья.")

    message += "\n".join(results)
    message += "\n\nИгра окончена. Спасибо за игру!"

    # We’ll finish the game and clear the file
    game_state['status'] = 'finished'
    save_game(game_state)
    send_message(message)

    # We’re clearing the file so we can start a new game
    clear_game()

if __name__ == "__main__":
    main()

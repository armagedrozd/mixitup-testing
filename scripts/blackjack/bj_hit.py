# -*- coding: utf-8 -*-
# bj_hit.py
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, __file__.rsplit('\\', 1)[0] if '\\' in __file__ else __file__.rsplit('/', 1)[0])
from bj_common import *

def main():
    username = """$username"""
    game_state = load_game()

    if not game_state or game_state['status'] != 'active':
        send_message(f"@{username}, сейчас нет активной игры.")
        return

    # Find the current player
    current_player_index = game_state['current_player_index']
    if current_player_index >= len(game_state['players']):
        # All players have finished; we’ll now move on to the dealer
        send_message("Все игроки закончили. Ожидайте ход дилера.")
        return

    current_player = game_state['players'][current_player_index]

    # We check that the command was issued by the current player
    if current_player['name'].lower() != username.lower():
        send_message(f"@{username}, сейчас не ваш ход. Ожидайте.")
        return

    # We check whether the player has finished
    if current_player['is_finished']:
        send_message(f"@{username}, вы уже закончили свой ход.")
        return

    # The player takes a card
    new_card = game_state['deck'].pop()
    current_player['hand'].append(new_card)
    current_player['value'] = calculate_hand_value(current_player['hand'])

    hand_str = hand_to_string(current_player['hand'])
    message = f"@{username}, вы берете карту: {card_to_string(new_card)}. Ваша рука: {hand_str} (Сумма: {current_player['value']})."

    # Checking for busted players
    if current_player['value'] > 21:
        current_player['is_finished'] = True
        message += " Перебор! Вы проиграли."
        # Let’s move on to the next player
        game_state['current_player_index'] += 1
        # Checking if there is a next player
        if game_state['current_player_index'] < len(game_state['players']):
            next_player = game_state['players'][game_state['current_player_index']]
            message += f" Ход игрока: @{next_player['name']}."
        else:
            # All players have finished; it’s the dealer’s turn to play
            # Call the function to play the dealer’s hand
            # (We’ll implement this as a separate command, ‘!bj dealer’, or automatically)
            message += " Все игроки закончили. Ход дилера."
            game_state['status'] = 'waiting_for_dealer'  # Новый статус

    elif current_player['value'] == 21:
        current_player['is_finished'] = True
        message += " У вас 21! Отлично."
        # Let’s move on to the next player
        game_state['current_player_index'] += 1
        if game_state['current_player_index'] < len(game_state['players']):
            next_player = game_state['players'][game_state['current_player_index']]
            message += f" Ход игрока: @{next_player['name']}."
        else:
            message += " Все игроки закончили. Ход дилера."
            game_state['status'] = 'waiting_for_dealer'

    # Сохраняем состояние
    save_game(game_state)
    send_message(message)

if __name__ == "__main__":
    main()

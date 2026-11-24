# -*- coding: utf-8 -*-
# bj_stand.py
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

    current_player_index = game_state['current_player_index']
    if current_player_index >= len(game_state['players']):
        send_message("Все игроки закончили. Ожидайте ход дилера.")
        return

    current_player = game_state['players'][current_player_index]

    if current_player['name'].lower() != username.lower():
        send_message(f"@{username}, сейчас не ваш ход.")
        return

    if current_player['is_finished']:
        send_message(f"@{username}, вы уже закончили свой ход.")
        return

    # The player stands
    current_player['is_finished'] = True
    hand_str = hand_to_string(current_player['hand'])
    message = f"@{username}, вы останавливаетесь. Ваша рука: {hand_str} (Сумма: {current_player['value']})."

    # Let’s move on to the next player
    game_state['current_player_index'] += 1

    if game_state['current_player_index'] < len(game_state['players']):
        next_player = game_state['players'][game_state['current_player_index']]
        message += f" Ход игрока: @{next_player['name']}."
    else:
        message += " Все игроки закончили. Ход дилера."
        game_state['status'] = 'waiting_for_dealer'

    save_game(game_state)
    send_message(message)

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
# bj_join.py
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, __file__.rsplit('\\', 1)[0] if '\\' in __file__ else __file__.rsplit('/', 1)[0])
from bj_common import *

def main():
    username = """$username"""
    game_state = load_game()

    if not game_state:
        send_message(f"@{username}, нет активной игры. Создайте ее с помощью '!bj start'.")
        return

    if game_state['status'] != 'lobby':
        send_message(f"@{username}, игра уже началась. Присоединиться нельзя.")
        return

    # Проверяем, не присоединился ли уже этот игрок
    for player in game_state['players']:
        if player['name'].lower() == username.lower():
            send_message(f"@{username}, вы уже в игре!")
            return

    # Добавляем игрока
    game_state['players'].append({
        'name': username,
        'hand': [],
        'value': 0,
        'is_finished': False,
        'has_blackjack': False
    })

    save_game(game_state)
    player_names = ', '.join([p['name'] for p in game_state['players']])
    send_message(f"@{username}, вы присоединились к игре! Текущие игроки: {player_names}. Когда все готовы, начните игру с помощью '!bj start'.")

if __name__ == "__main__":
    main()


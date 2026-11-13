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

    # Находим текущего игрока
    current_player_index = game_state['current_player_index']
    if current_player_index >= len(game_state['players']):
        # Все игроки закончили, переходим к дилеру
        send_message("Все игроки закончили. Ожидайте ход дилера.")
        return

    current_player = game_state['players'][current_player_index]

    # Проверяем, что команду вызвал текущий игрок
    if current_player['name'].lower() != username.lower():
        send_message(f"@{username}, сейчас не ваш ход. Ожидайте.")
        return

    # Проверяем, не закончил ли игрок (не перебор или не stand)
    if current_player['is_finished']:
        send_message(f"@{username}, вы уже закончили свой ход.")
        return

    # Игрок берет карту
    new_card = game_state['deck'].pop()
    current_player['hand'].append(new_card)
    current_player['value'] = calculate_hand_value(current_player['hand'])

    hand_str = hand_to_string(current_player['hand'])
    message = f"@{username}, вы берете карту: {card_to_string(new_card)}. Ваша рука: {hand_str} (Сумма: {current_player['value']})."

    # Проверяем на перебор
    if current_player['value'] > 21:
        current_player['is_finished'] = True
        message += " Перебор! Вы проиграли."
        # Переходим к следующему игроку
        game_state['current_player_index'] += 1
        # Проверяем, есть ли следующий игрок
        if game_state['current_player_index'] < len(game_state['players']):
            next_player = game_state['players'][game_state['current_player_index']]
            message += f" Ход игрока: @{next_player['name']}."
        else:
            # Все игроки закончили, нужно играть дилеру
            # Вызываем функцию для игры дилера
            # (Мы реализуем это в отдельной команде '!bj dealer' или автоматически)
            message += " Все игроки закончили. Ход дилера."
            # Здесь мы можем вызвать логику дилера, но для простоты
            # мы предложим игрокам написать '!bj dealer'
            game_state['status'] = 'waiting_for_dealer'  # Новый статус

    elif current_player['value'] == 21:
        current_player['is_finished'] = True
        message += " У вас 21! Отлично."
        # Переходим к следующему игроку
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

# -*- coding: utf-8 -*-
# bj_start.py (Исправленная версия)
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, __file__.rsplit('\\', 1)[0] if '\\' in __file__ else __file__.rsplit('/', 1)[0])
from bj_common import *

def main():
    username = """$username"""
    game_state = load_game()

    # Случай 1: Игры нет. Создаем новую.
    if not game_state:
        game_state = {
            'status': 'lobby',
            'deck': create_deck(),
            'players': [{'name': username, 'hand': [], 'value': 0, 'is_finished': False, 'has_blackjack': False}],
            'dealer_hand': [],
            'current_player_index': 0,
            'message': ''
        }
        save_game(game_state)
        send_message(f"@{username}, игра в Blackjack создана! Присоединяйтесь с помощью '!bj join'. Когда все готовы, напишите '!bj start' еще раз, чтобы начать игру.")
        return

    # Случай 2: Игра в лобби. Начинаем раздачу.
    if game_state['status'] == 'lobby':
        # Проверяем, есть ли игроки
        if len(game_state['players']) == 0:
            send_message("Нельзя начать игру без игроков.")
            clear_game()
            return

        # Раздаем по 2 карты каждому игроку и дилеру
        for player in game_state['players']:
            player['hand'] = [game_state['deck'].pop(), game_state['deck'].pop()]
            player['value'] = calculate_hand_value(player['hand'])
            if player['value'] == 21:
                player['has_blackjack'] = True

        # Дилер получает 2 карты, но мы показываем только одну
        game_state['dealer_hand'] = [game_state['deck'].pop(), game_state['deck'].pop()]
        dealer_value = calculate_hand_value(game_state['dealer_hand'])

        game_state['status'] = 'active'
        game_state['current_player_index'] = 0

        # Сохраняем состояние
        save_game(game_state)

        # Формируем сообщение о начале игры
        players_info = []
        for player in game_state['players']:
            hand_str = hand_to_string(player['hand'])
            players_info.append(f"@{player['name']} ({player['value']}): {hand_str}")

        # Показываем первую карту дилера
        dealer_first_card = card_to_string(game_state['dealer_hand'][0])
        dealer_hidden = "🂠"  # Символ рубашки карты

        message = f"Игра началась! Карты:\n"
        message += "\n".join(players_info)
        message += f"\nДилер: {dealer_first_card}, {dealer_hidden}"

        # Проверяем на мгновенный блэкджек у игроков
        blackjack_players = [p['name'] for p in game_state['players'] if p['has_blackjack']]
        if blackjack_players:
            message += f"\n\nБлэкджек у игроков: {', '.join(blackjack_players)}!"
            for p in blackjack_players:
            	add_WINNERS_to_file(p['name'])
            # Здесь нужно обработать выплаты, но для простоты просто объявим победителей
            # и завершим игру.
            # TODO: Добавить логику выплат и завершения.
            game_state['status'] = 'finished'
            save_game(game_state)
            message += "\nИгра окончена! Победители получают выплаты."
            # Очищаем игру после небольшой задержки? Нет, оставим для следующей команды.
            clear_game()
            send_message(message)
            return

        # Если нет блэкджека, начинаем ход первого игрока
        current_player = game_state['players'][0]
        message += f"\n\nХод игрока: @{current_player['name']}. Ваши действия: '!bj hit' или '!bj stand'."
        send_message(message)
        return

    # Случай 3: Игра уже идет.
    if game_state['status'] == 'active':
        send_message(f"@{username}, игра уже идет. Дождитесь ее окончания.")
        return

    # Случай 4: Игра завершена.
    if game_state['status'] == 'finished':
        send_message(f"@{username}, предыдущая игра завершена. Начните новую с помощью '!bj start'.")
        return

if __name__ == "__main__":
    main()

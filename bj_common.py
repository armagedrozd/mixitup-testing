# bj_common.py
import json
import os
import random
import sys

# Определяем путь к файлу состояния игры
# Предполагаем, что скрипты находятся в одной папке
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GAME_FILE = os.path.join(SCRIPT_DIR, 'bj_game.json')
WINNERS = r"file path"
LOSERS = r"file path"

# --- Работа с картами ---

def create_deck():
    """Создает и перемешивает стандартную колоду из 52 карт."""
    suits = ['♠️', '♥️', '♦️', '♣️']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def card_value(card):
    """Возвращает стоимость карты для подсчета очков."""
    if card['rank'] in ['J', 'Q', 'K']:
        return 10
    elif card['rank'] == 'A':
        return 11  # Возвращаем 11, но будем обрабатывать особый случай для туза
    else:
        return int(card['rank'])

def calculate_hand_value(hand):
    """Подсчитывает стоимость руки, учитывая, что туз может быть 1 или 11."""
    value = 0
    aces = 0
    for card in hand:
        val = card_value(card)
        if val == 11:
            aces += 1
        value += val

    # Если у нас есть тузы и значение больше 21, превращаем тузы из 11 в 1
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

def card_to_string(card):
    """Преобразует карту в строку для вывода в чат."""
    return f"{card['rank']}{card['suit']}"

def hand_to_string(hand):
    """Преобразует руку в строку для вывода."""
    return ', '.join([card_to_string(card) for card in hand])

# --- Работа с файлом состояния ---

def load_game():
    """Загружает состояние игры из файла. Если файла нет, возвращает None."""
    if os.path.exists(GAME_FILE):
        with open(GAME_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def save_game(game_state):
    """Сохраняет состояние игры в файл."""
    with open(GAME_FILE, 'w', encoding='utf-8') as f:
        json.dump(game_state, f, ensure_ascii=False, indent=4)

def clear_game():
    """Удаляет файл состояния игры."""
    if os.path.exists(GAME_FILE):
        os.remove(GAME_FILE)

# --- Функции для вывода сообщений ---

def send_message(message):
    """Выводит сообщение в чат. Mix It Up захватывает stdout."""
    print(message)

def send_error(message):
    """Выводит сообщение об ошибке."""
    print(f"[Ошибка] {message}")

def get_username():
    """Получает имя пользователя из аргумента или из $username."""
    # В Mix It Up мы передаем имя пользователя как аргумент
    # Это делается для того, чтобы скрипт был универсальным.
    # Если аргумент не передан, пытаемся использовать $targetusername
    # Но лучше всегда передавать $username первым аргументом.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "Unknown"
    
def add_WINNERS_to_file(user_id: str) -> bool:
    """
    Добавляет ID в файл. Возвращает True, если добавлен, False если уже был.
    """
    user_id = str(user_id).strip()  
    # Проверяем, есть ли уже
    if os.path.exists(WINNERS):
        with open(WINNERS, "r", encoding="utf-8") as f:
            existing = {line.strip() for line in f}
        if user_id in existing:
            print(f"SKIP: {user_id} already exists")
            return False
    
    # Добавляем
    with open(WINNERS, "a", encoding="utf-8") as f:
        f.write(user_id + "\n")
    return True

def add_LOSERS_to_file(user_id: str) -> bool:
    """
    Добавляет ID в файл. Возвращает True, если добавлен, False если уже был.
    """
    user_id = str(user_id).strip()
        
    # Проверяем, есть ли уже
    if os.path.exists(LOSERS):
        with open(LOSERS, "r", encoding="utf-8") as f:
            existing = {line.strip() for line in f}
        if user_id in existing:
            print(f"SKIP: {user_id} already exists")
            return False
    
    # Добавляем
    with open(LOSERS, "a", encoding="utf-8") as f:
        f.write(user_id + "\n")
    return True
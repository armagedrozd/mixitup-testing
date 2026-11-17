# mixitup-testing
QA Portfolio: Testing Extensions for Mixitup (Chat-Bot)

Hi! This is my portfolio, where I showcase my testing skills using my own extensions for Mixitup—a middleware program that manages live streams via the APIs of Twitch, YouTube, and other services.

## 🎯 Project Goal
To demonstrate how I test **my own functionality** integrated into a third-party platform. Unlike testing “someone else’s website using a checklist,” here I wrote the code myself (for example, a “Blackjack” mini-game in Python), integrated it into Mixitup myself, and tested how it works under real-world streaming conditions myself.

## 🛠️ Skills Demonstrated by the Project
- **Testing In-House Development**: Testing the Python scripts built into Mixitup in conjunction with the Twitch API.
- **Test design**: equivalence classes, boundary values, usage scenarios (for example, what happens if a viewer types a command in the chat during a game).
- **Documentation**: test cases, checklists, and bug reports for the project’s own functionality.
- **Working with External APIs**: understanding how Mixitup interacts with Twitch and YouTube (requests, responses, delays, authorization errors).
- **Tools**: Git/GitHub, DevTools (Network, Console), Mixitup logs.

## 📂 Repository Structure
- `/scripts` — Python scripts (such as the ‘/blackjack’ mini-game) that I wrote to extend Mixitup's functionality.
- `/test-documentation` — test cases, checklists, and bug reports for these scripts.
- `README.md` — this file.

## 🎲 Extension Example: “Blackjack” Mini-Game
One of the extensions in the `/scripts` folder is the “Blackjack” game, which I implemented using chatbot functionality. Viewers type commands into the Twitch chat, Mixitup passes them to my script, the script handles the game logic, and returns a response back to the chat. The `/test-documentation` folder describes how I tested this game: from ensuring the score is calculated correctly to how it behaves when multiple viewers play simultaneously.

### 🧩 The Architecture of the “Blackjack” Game
The game is implemented not as a single file, but as **six modules**, each of which is responsible for its own segment of logic and is called by a separate command in the chat. This makes it easy to expand the game and test each module in isolation.

## 🚀 How It Works (In Brief)
1. Mixitup runs my Python script as an extension.
2. The script subscribes to chat events (via the Mixitup/Twitch API).
3. When a viewer types a command, the script processes it and returns the result to the chat.
4. I test every step: what the script received, what it returned, and what the viewer saw.

## 📝 What's Inside the Documentation
In the `/test-documentation` folder, you'll find:
- **Test cases** for verifying the bot's commands (e.g., “start the game,” “draw a card,” “stop”).
- **Checklists** for quickly verifying the script’s functionality after changes.
- **Sample bug reports** with steps to reproduce the issue (for example, “When two spectators play simultaneously, the first spectator’s score is reset”).

## ⚠️ Limitations and Plans
- **Not covered**: Testing the Twitch API itself (this is a separate project, since the API belongs to Twitch, not Mixitup).
- **Not covered**: Load testing (how many viewers can play “Blackjack” simultaneously without losing messages).
- **Planned**: Add test cases for other scripts.

## 📬 Contact
- Email: krbyte@yandex.ru
- GitHub: https://github.com/armagedrozd

A detailed description of each module, their commands, and areas of responsibility can be found in [`/scripts/README.md`](scripts/README.md).



# QA-портфолио: тестирование расширений для Mixitup (Чат-бот)

Привет! Это мое портфолио, где я демонстрирую навыки тестирования на примере собственных расширений для Mixitup — программы-посредника, которая через API Twitch, YouTube и других сервисов управляет прямыми трансляциями.

## 🎯 Цель проекта
Показать, как я тестирую **свой собственный функционал**, встроенный в стороннюю платформу. В отличие от тестирования «чужого сайта по чек-листу», здесь я сам написал код (например, мини-игру «Блэкджек» на Python), сам встроил его в Mixitup и сам же проверил, как он работает в реальных условиях трансляции.

## 🛠️ Навыки, которые демонстрирует проект
- **Тестирование собственной разработки**: проверка Python-скриптов, встроенных в Mixitup, в связке с API Twitch.
- **Тест-дизайн**: классы эквивалентности, граничные значения, сценарии использования (например, что будет, если зритель напишет команду в чат во время игры).
- **Документация**: тест-кейсы, чек-листы, баг-репорты для собственного функционала.
- **Работа с внешними API**: понимание того, как Mixitup взаимодействует с Twitch и YouTube (запросы, ответы, задержки, ошибки авторизации).
- **Инструменты**: Git/GitHub, DevTools (Network, Console), логи Mixitup.

## 📂 Структура репозитория
- `/scripts` — Python-скрипты (например, мини-игра ‘/blackjack’), которые я написал для расширения функционала Mixitup.
- `/test-documentation` — тест-кейсы, чек-листы и баг-репорты для этих скриптов.
- `README.md` — этот файл.

## 🎲 Пример расширения: мини-игра «Блэкджек»
Одно из расширений в папке `/scripts` — это игра «Блэкджек», которую я реализовал через функционал чат-бота. Зрители пишут команды в чат Twitch, Mixitup передает их моему скрипту, скрипт обрабатывает логику игры и возвращает ответ обратно в чат. В папке `/test-documentation` описано, как я тестировал эту игру: от корректности подсчета очков до поведения при одновременной игре нескольких зрителей.

## 🚀 Как это работает (кратко)
1. Mixitup запускает мой Python-скрипт как расширение.
2. Скрипт подписывается на события чата (через API Mixitup/Twitch).
3. Когда зритель пишет команду, скрипт обрабатывает её и возвращает результат в чат.
4. Я тестирую каждый шаг: что скрипт получил, что он вернул, что увидел зритель.

## 📝 Что внутри документации
В папке `/test-documentation` вы найдете:
- **Тест-кейсы** для проверки команд бота (например, «начать игру», «взять карту», «остановиться»).
- **Чек-листы** для быстрой проверки работоспособности скрипта после изменений.
- **Примеры баг-репортов** с шагами воспроизведения (например, «при одновременной игре двух зрителей счет первого сбрасывается»).

## ⚠️ Ограничения и планы
- **Не покрыто**: тестирование самого API Twitch (это тема отдельного проекта, так как API принадлежит Twitch, а не Mixitup).
- **Не покрыто**: нагрузочное тестирование (сколько зрителей может одновременно играть в «Блэкджек» без потери сообщений).
- **В планах**: добавить тест-кейсы для других скриптов.
## 📬 Контакты
- Email: ваш email
- GitHub: ссылка на ваш профиль

### 🧩 Архитектура игры «Блэкджек»
Игра реализована не одним файлом, а **шестью модулями**, каждый из которых отвечает за свой сегмент логики и вызывается отдельной командой из чата. Это позволяет легко расширять игру и тестировать каждый модуль изолированно.

Подробное описание каждого модуля, их команд и зон ответственности — в [`/scripts/README.md`](scripts/README.md).


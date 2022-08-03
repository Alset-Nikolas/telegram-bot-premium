# telegram-bot-premium
    Yandex backend school (Архитектура кода)

### Идея:
     Написать бота с разделением людей (премиальные и обычные).

## Для запуска необходимо установить свой токен (ключ)
    1. Создать папку в telegram-premium/secrets
    2. В новой папке secrets создать файл secret.txt
    3. В файле прописть свой TOKEN (для своего бота) - 1 строчка

## Запуск в терминале
    1. cd telegram-premium
    2. python3 main.py --token $(cat secrets/secret.txt)

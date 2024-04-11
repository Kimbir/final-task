import random

def input_players():

    #Функция запрашивает имена игроков и возвращает список их имен.

    players = []
    while True:
        player_name = input("Введите имя игрока (или нажмите Enter для завершения): ")
        if player_name:
            players.append(player_name)
        else:
            break
    return players

def generate_number(min_value, max_value):

    #Функция генерирует случайное число в заданном диапазоне.

    return random.randint(min_value, max_value)

def find_winner(guesses, target_number):

    #Функция определяет победителя на основе предположений игроков и загаданного числа.

    closest_guess = None
    min_difference = float('inf')
    equal_min_diff = False
    for player, guess in guesses.items():
        difference = abs(guess - target_number)
        if difference < min_difference:
            min_difference = difference
            closest_guess = player
            equal_min_diff = False
        elif difference == min_difference:
            equal_min_diff = True
    if equal_min_diff:
        return None
    return closest_guess

def guess_the_number():

    #Основная функция игры "Угадай число".

    print("Добро пожаловать в игру Угадай число!")
    players = input_players()
    if not players:
        print("Нет игроков. Игра завершена.")
        return

    min_value = int(input("Введите минимальное значение для загадываемого числа: "))
    max_value = int(input("Введите максимальное значение для загадываемого числа: "))
    target_number = generate_number(min_value, max_value)
    print(f"Число загадано в диапазоне от {min_value} до {max_value}.")

    guesses = {}
    for player in players:
        guess = int(input(f"{player}, угадайте число: "))
        guesses[player] = guess

    winner = find_winner(guesses, target_number)
    if winner is None:
        print("Ничья! Слишком много игроков с одинаковым минимальным расстоянием до числа.")
    else:
        print(f"Число было загадано: {target_number}")
        print(f"Победитель: {winner}, его предположение: {guesses[winner]}")
        print("Поздравляем победителя!")

        for player, guess in guesses.items():
            if player != winner:
                print(f"{player}, Вы не угадали. Попробуйте еще раз!")

guess_the_number()

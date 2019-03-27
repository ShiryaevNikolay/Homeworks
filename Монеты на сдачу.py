# -----------↓↓↓Делаем проверку на ввод числа.↓↓↓
while True:
    try:
        number_of_change = int(input("Введите кол-во монет, которые должен отдать кассир: "))
        if number_of_change > 0:
            break
        elif number_of_change == 0:
            print("Сдача вам не нужна.")
            break
        else:
            print("Необходиммо ввести целое неотрицательно число")
    except ValueError:
        print("Некорректный ввод. Введите целое неотрицательное число.")


# ---------------↑↑↑Проверка на ввод числа.↑↑↑


def counting_the_number_of_coins(coins, change):
    # "coins += 1" - считает, сколько нужно монет для сдачи
    if change == 0:
        return print(coins)
    elif change >= 50:  # Проверка, можно ли дать сдачу 50-ю копейками
        coins += 1
        change -= 50
        counting_the_number_of_coins(coins, change)
    elif change >= 10:  # Проверка, можно ли дать сдачу 10-ю копейками
        coins += 1
        change -= 10
        counting_the_number_of_coins(coins, change)
    elif change >= 5:  # Проверка, можно ли дать сдачу 5-ю копейками
        coins += 1
        change -= 5
        counting_the_number_of_coins(coins, change)
    elif change >= 1:  # Проверка, можно ли дать сдачу 1-ой копейкой
        coins += 1
        change -= 1
        counting_the_number_of_coins(coins, change)


if number_of_change > 0:
    print("Минимальное количество монет, которые должен отдать кассир: ")
    counting_the_number_of_coins(0, number_of_change)

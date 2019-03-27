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
    if change == 0:
        return print(coins)
    elif change >= 50:
        coins += 1
        change -= 50
        counting_the_number_of_coins(coins, change)
    elif change >= 10:
        coins += 1
        change -= 10counting_the_number_of_coins(coins, change)
    elif change >= 5:
        coins += 1
        change -= 5counting_the_number_of_coins(coins, change)
    elif change >= 1:
        coins += 1
        change -= 1counting_the_number_of_coins(coins, change)


if number_of_change > 0:
    print("Минимальное количество монет, которые должен отдать кассир: ")
    counting_the_number_of_coins(0, number_of_change)
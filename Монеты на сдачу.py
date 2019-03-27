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


def check_the_number_of_coins(coins, change):
    if change > 50 and change > 0:
        coins += 1
        change -= 50
        check_the_number_of_coins(coins, change)
    elif change > 10 and change > 0:
        coins += 1
        change -= 10
        check_the_number_of_coins(coins, change)
    elif change > 5 and change > 0:
        coins += 1
        change -= 5
        check_the_number_of_coins(coins, change)
    elif change > 1 and change > 0:
        coins += 1
        change -= 1
        check_the_number_of_coins(coins, change)
    else:
        coins += 1
        return print(coins)


if number_of_change > 0:
    print("Минимальное количество монет, которые должен отдать кассир: ")
    check_the_number_of_coins(0, number_of_change)
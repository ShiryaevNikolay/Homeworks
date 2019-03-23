while True:
    try:
        n = int(input("height: "))
        if n > 0 and n < 24:
            break
        else:
            print("Введите число в пределах от 1 до 23.")
    except ValueError:
        print("Некорректный ввод! Введите положительное целое число.")


tab = " "
for i in range(n):
    if i == n - 1:
        tab = ""
    else:
        tab = " "
    tab = tab * (n - i - 1)
    for j in range(i + 2):
        tab += "#"
    print(tab)
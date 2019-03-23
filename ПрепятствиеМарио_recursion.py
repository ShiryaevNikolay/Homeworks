while True:
    try:
        n = int(input("height: "))
        if n > 0 and n < 24:
            break
        else:
            print("Введите число в пределах от 1 до 23.")
    except ValueError:
        print("Некорректный ввод! Введите положительное целое число.")


maxL = n             #запоминаем высоту
def town(n):
    tab = " "
    if n == 0:
        return
    else:
        town(n - 1)
        if n == maxL:
            tab = ""
        else:
            tab = " "
        tab = tab * (maxL - n)     #добавляем нужное кол-во отступов слева
        for j in range(n + 1):
            tab += "#"             #добавляем нужное кол-во блоков
        print(tab)


town(n)
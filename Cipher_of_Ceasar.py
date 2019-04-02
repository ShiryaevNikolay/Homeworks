""" Documentation:
       letter - текст, который нужно зашифровать
       key - ключ
       cipher - шифр """


letter = str(input("Введите послание на русском, которое нужно зашифровать: "))
letter = letter.strip()                                                 # Форматирование
letter = letter.lower()                                                 # текста


while True:                                      #
    try:                                         #
        key = int(input("Введите ключ: "))       # Проверка
        break                                    # ввода
    except ValueError:                           # ключа
        print("Ключ должен быть целым числом.")  #


alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


cipher = ""
for i in letter:
    try:                                                                #
        i = int(i) + key                                                #
        if i < 10:                                                      # Шифрование
            cipher += str(i)                                            # цифры
        else:                                                           #
            i = i % 10                                                  #
            cipher += str(i)                                            #
    except ValueError:
        cipher += alphabet[(alphabet.index(i) + key) % len(alphabet)]   # Шифрование буквы


print('Шифр: "' + cipher + '"') # Вывод шрифта на экран

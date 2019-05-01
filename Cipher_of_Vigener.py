import re

letter = input("Enter the text in Russian, which must be encrypted: ");


while(True):
    try:
        key = input("Enter the secret word in Russian: ")
        break
    except:
        print("Invalid key entered.")

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
two = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

cipher = ""
j = 0
for i in letter:
    if re.search(r"[0-9]", i):
        cipher += i
    else:
        if i == " ":
            cipher += " "
        else:
            if re.search(r"[А-Я]", i):
                cipher += two[(two.index(i) + alphabet.index(key[j])) % 33]
            else:
                cipher += alphabet[(alphabet.index(i) + alphabet.index(key[j])) % 33]
            if j == len(key) - 1:
                j = 0
            else:
                j += 1

print("Cipher: " + cipher)
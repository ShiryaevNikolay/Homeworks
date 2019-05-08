while True:
    try:
        n = int(input("Enter the size of area (3 or 4): "))
        if n == 3 or n == 4:
            break
    except:
        print("Invalid input. Enter a positive integer.")

area = []


def init():
    value = n * n - 1
    for i in range(n):
        area.append([])
        for j in range(n):
            area[i].append(value)
            value -= 1
    if n == 4:
        area[3][1], area[3][2] = area[3][2], area[3][1]


def draw():
    if n == 4:
        print("________________")
    else:
        print("___________")
    print("")
    for i in range(n):
        for j in range(n):
            if area[i][j] == 0:
                print(" _", " ", end="")
            elif area[i][j] > 0 and area[i][j] <= 9:
                print("", area[i][j], " ", end="")
            else:
                print("", area[i][j], "", end="")
        print("\n")


def move(step):
    for i in range(n):
        for j in range(n):
            if area[i][j] == 0:
                break
        if area[i][j] == 0:
            break
    if step == "w":
        if i != n - 1:
            area[i][j], area[i + 1][j] = area[i + 1][j], area[i][j]
    elif step == "d":
        if j != 0:
            area[i][j], area[i][j - 1] = area[i][j - 1], area[i][j]
    elif step == "s":
        if i != 0:
            area[i][j], area[i - 1][j] = area[i - 1][j], area[i][j]
    elif step == "a":
        if j != n - 1:
            area[i][j], area[i][j + 1] = area[i][j + 1], area[i][j]
    else:
        return print("Unable to make a move.")


def won():
    value = 1
    win = 0
    f = 1
    for i in range(n):
        for j in range(n):
            if i == n - 1 and j == n - 1:
                value = 0
            if area[i][j] != value:
                f = 0
            value += 1
    if f == 1:
        win = 1
    return win


""" Available steps:
        w, d, s, a"""

init()
draw()
w = won()
while w == 0:
    step = input("Enter a step: ")
    step.lower()
    move(step)
    draw()
    w = won()
print("YOU WIN !")

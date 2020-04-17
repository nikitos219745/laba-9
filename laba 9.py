import numpy as np
import random
import timeit


def bub_sort(mlist):
    exchange = 0
    count = 0
    lst_item = len(mlist) - 1                  # діапазон до передостаннього елементу
    for i in range(0, lst_item):
        for x in range(0, lst_item):                            # починаємо перевірки з першого елементу, з кожним порівнянням діапазон скорочується    
            count += 1                              #к-ль порівнянь
            if mlist[x] > mlist[x + 1]:                               #перевірка елемента  з наступним
                mlist[x], mlist[x + 1] = mlist[x + 1], mlist[x]                #якщо більше  то виконуєм заміну
                exchange += 1
    print("число порівнянь:", count)                    #вивід значення
    print("чсло обмінів:", exchange)                  #вивід значення
    print(" ")

    return list


def selection_sort(array):
    exchanger = 0
    counter = 0
    for i in range(len(array) - 1):          # діапазон до передостаннього елементу
        counter += 1       #к-ль порівнянь
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:      #задання умови
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]         #якщо масив J less than M міняємо місцями
        exchanger += 1                     #к-ль обмінів
    print("число порівнянь:", counter)
    print("чсло обмінів:", exchanger)
    return array                      #повертаєм масив


def insertion(data):             #створення ф-ї
    exchanger = 0                #к-ль перестановок
    counter = 0                 #к-ль порівнянь
    for i in range(len(data)):      
        counter += 1
        j = i - 1
        key = data[i]                   #Присвоєння елемента ключу,як пізніше збережеться на новому місці           
        while data[j] > key and j >= 0:#задання умови при якій буде відбуватись заміна
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key            #заміна елементів
        exchanger += 1
    print("число порівнянь:", counter - 1)
    print("чсло обмінів:", exchanger)
    return data

while True:
    while True:
        try:
            choose = int(input("bubble sort - 1,selection sort - 2,insertion sort - 3,ваш вибір: "))
            if choose <= 3:
                break
            else:
                choose = int(input("bubble sort - 1,selection sort - 2,insertion sort - 3,ваш вибір: "))
                break
        except ValueError:
            print("тільки цифри")
    flag = input(
        "Если вы хотите рандомизировать входные данные, нажмите «Enter». Для ввода вручную нажмите любую другую клавишу: ")
    print("")
    if flag == "":
        while True:
            try:
                b = int(input("Введіть кількість яка буде генеруватися: "))
                break
            except ValueError:
                print("Тільки цифри")
        a = np.zeros(b, dtype=int)
        while True:
            try:
                d1 = int(input('Ліва грань: '))  #задання границь
                d2 = int(input('Права грань: ')) #задання границь
                break
            except ValueError:
                print("тільки цифри")
        for i in range(b):
            a[i] = random.randint(d1, d2)

    else:
        while True:
            try:
                b = int(input("Введіть кількість яка буде генеруватися: "))
                if b <= 30:
                    break
                else:
                    b = int(input("Введіть кількість яка буде генеруватися: "))
            except ValueError:
                print("тільки цифри")
        a = np.zeros(b, dtype=int)
        for i in range(b):
            a[i] = int(input(f'Enter {i + 1} element: '))

    if choose == 1:                #задання умови на вибір методу сортування
        print("Старий список", a)
        print(" ")

        new = bub_sort(a)
        print("Відсортований від меншого до більшого", new)
        print(" ")

        s = np.array(a)
        x = s[::-1]
        print("Від більшого до меншого", x)
        print(" ")



    if choose == 2:                                    #задання умови на вибір методу сортування
        print("Старий список", a)
        print(" ")
        new = selection_sort(a)
        print("Відсортований від меншого до більшого", new)
        print(" ")
        s = np.array(a)
        x = s[::-1]                                 #за допомогою зрізу виводим елементи навпаки
        print("Від більшого до меншого", x)
        print(" ")


    if choose == 3:                              #задання умови на вибір методу сортування
        print("Старий список", a)
        print(" ")
        new = insertion(a)
        print("відсортований від меншого до більшого", new)
        print(" ")
        s = np.array(a)
        x = s[::-1]                                         #за допомогою зрізу виводим елементи навпаки
        print("Від більшого до меншого", x)
        print(" ")

    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(f"Програма виконувалась {t} секунд")
    print(" ")
    if input('Натисни "Enter"  для перезавантаження: ') == '':
        continue
    break

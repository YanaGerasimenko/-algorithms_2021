"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]


left.clear()
right.clear()


m = 3
len = 7
i
left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""

from statistics import median

from random import randint

from timeit import timeit


def gnome_sort(ls):

    i, size = 1, len(ls)

    m = size // 2

    while i < size:

        if ls[i - 1] <= ls[i]:

            i += 1

        else:

            ls[i - 1], ls[i] = ls[i], ls[i - 1]

            if i > 1:

                i -= 1

    return ls[m]


def median_sort(ls):

    ls.sort()

    n = len(ls)

    assert n % 2 == 1

    return ls[n // 2]


def max_median(ls):

    l = ls

    for i in range(0, len(ls) // 2):

        l.remove(max(l))

    return max(l)


l = [randint(1, 100) for _ in range(11)]

print('Список: ', l)

print('Встроенная функция: ', median(l))

print(timeit("median(l[:])", globals=globals(), number=1000))

print('Гномья сортировка: ', gnome_sort(l))

print(timeit("gnome_sort(l[:])", globals=globals(), number=1000))

print('Функция c использованием сортировки: ', median_sort(l))

print(timeit("median_sort(l[:])", globals=globals(), number=1000))

print('Функция max: ', max_median(l))

print(timeit("max_median(l[:])", globals=globals(), number=1000))


"""
-----------------------------------------------------------------------------------------------------------------------
Исходя из результатов (по убыванию):
1. Функция с сортировкой
2. Встроенная медиана
3. Гномья сортировка
4. Max
(Убедиться можно в результатах)
-----------------------------------------------------------------------------------------------------------------------
Результаты:
-----------------------------------------------------------------------------------------------------------------------
Перввый пробег
-----------------------------------------------------------------------------------------------------------------------
Список: [39, 90, 91, 68, 56, 60, 69, 79, 90, 89, 67]
Встроенная функция:  69
0.0004804999999999948
Гномья сортировка:  69
0.0009617000000000028
Функция c использованием сортировки:  69
0.0002994999999999942
Функция max:  69
0.0011499999999999982
-----------------------------------------------------------------------------------------------------------------------
Второй пробег
-----------------------------------------------------------------------------------------------------------------------
Список: [8, 67, 32, 8, 65, 84, 82, 43, 81, 57, 53]
Встроенная функция:  57
0.00046169999999999545
Гномья сортировка:  57
0.0009812000000000015
Функция c использованием сортировки:  57
0.00029730000000000034
Функция max:  57
0.0011450000000000002
-----------------------------------------------------------------------------------------------------------------------
Третий пробег
-----------------------------------------------------------------------------------------------------------------------
Список:  [61, 5, 97, 11, 65, 74, 49, 75, 17, 14, 18]
Встроенная функция:  49
0.0004880000000000023
Гномья сортировка:  49
0.0010107000000000033
Функция c использованием сортировки:  49
0.0002944000000000002
Функция max:  49
0.0012810999999999934
-----------------------------------------------------------------------------------------------------------------------
"""

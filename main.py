# name = "Anna"
# print("Hello", name)
# age = 24
# print(age)
# print(id(age))
import random
# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, 'Hello', 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)

# a = '6'
# b = 2
# print(int(a) + b)

# a = 1
# b = 2
# print('a =', a)
# print('b =', b)
# c = a
# a = b
# b = c
# a = a + b
# b = a - b
# a = a - b

# summa = 5 + 7 + 3
# pr = 5 * 7 * 3
# sr = (5 + 7 + 3)/3
# print('Сумма: ', summa, '\nПроизведение: ', pr,  '\nСреднее арифметическое: ', sr)


# num = 4321
# a = num % 10
# print(a)
# b = (num // 10) % 10
# print(b)
# c = (num // 100) % 10
# print(c)
# d = (num // 1000) % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)
#
# num1 = '2'
# num2 = 3
# res = num1 + str(num2)
# print(res)


# print(int(3.8))
# print(round(3.8))
# print(round(3.891, 2))

# name = 'Виктор'
# age = 28
# print('Меня зовут ' , name ,'. мне' , age , 'лет', sep='--')
# print('Я учу Python.')

# name = input('Введите ваше имя: ')
# print('Hello', name)

# a = input('Введите число: ')
# b = input('Укажите степень: ')
# res = int(a)**int(b)
# print(res)

# b1 = True
# b2 = False
# print(b1 + 5)

# print(bool('Python'))
# print(bool('')) # False
# print(bool(' ')) # True

# cnt = 15
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input('Введите совй возраст: '))
# if age >= 18:
#     print('Доступ на сайт разрешен')
# else:
#     print('Доступ запрещен')

# a = 15
# b = 5
# if a > b:
#     print('a > b')
# elif b > a:
#     print('a < b')
# else:
#     print('a == b')

# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or b == c or a == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# day = int(input('Введите день недели цифрой: '))
# if day >= 1 and day <= 5:
#     print('рабочий день - ', end='')
#     if day == 1:
#         print('понедельник')
#     if day == 2:
#         print('вторник')
#     if day == 3:
#         print('среда')
#     if day == 4:
#         print('четверг')
#     if day == 5:
#         print('пятница')
# elif day == 6 or day == 7:
#     print('выходной день - ', end='')
#     if day == 6:
#         print('суббота')
#     if day == 7:
#         print('воскресенье')
# else:
#     print('такого дня недели не сущетсвует')

# month = int(input('Введите номер месяца (цифрой): '))
# if month == 12 or month == 1 or month == 2:
#     print('Зима')
# elif 3 <= month <= 5:
#     print('Весна')
# elif 6 <= month <= 8:
#     print('Лето')
# elif 9 <= month <= 11:
#     print('Осень')
# else:
#     print('Ошибка ввода данных')

# n = int(input('Сколько ворон на ветке от 0 до 9: '))
# if 0 <= n <= 9:
#     print('На ветке ', n, end='')
#     if n==1:
#         print(' ворона')
#     elif 2<=n<=4:
#         print(' вороны')
#     elif 5<=n<=9 or n == 0:
#         print(' ворон')
# else:
#     print('Ошибка ввода')

# password = 'moderato'
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print('Пароль не верен')

# day = 'вторник'
# time = 16
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 10, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = int(input('Введите 1 число'))
# b = int(input('Введите 2 число'))
# print(a // b if b != 0 else 'На нуль делить нельзя')

# a = 0
# b = '2a'
# print(a + int(b))

# try:
#     n = int(input('Введите целое число: '))
#     print(n * 2)
# except ValueError:
#     print('Что то пошло не так')

# zn1 = int(input('Введите первое число: '))
# zn2 = int(input('Введите второе число: '))
# try:
#     print(zn1 + zn2)
# except ValueError:
#     print(zn1 + zn2)

# i = 0
# while i < 5:
#     print('i = ', i)
#     i += 1

# i = 2
# while i <= 20:
#     print('i = ', i)
#     i += 2


# x = int(input('Введите количество символов: '))
# i = 0
# while i < x:
#     print('*', end='')
#     i += 1

# try:
#     x = int(input('Количество: '))
#     while x > 0:
#         print('*', end='')
#         x -= 1
# except ValueError:
#     print('Введите число!')

# a = int(input('Начало диапазона: '))
# b = int(input('Конец диапазона: '))
# if a % 2 == 0:
#     a += 1
# sum1 = 0
# while a <= b:
#     sum1 += a
#     a += 2;
# print('Сумма нечетных: ', sum1)

# n = input('Введите целое число: ')
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число: ')
# if n % 2 == 0:
#     print('Четное число!')
# else:
#     print('Нечетное число!')

# i = 0
# while i < 10:
#     if i == 3:
#         i+= 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input('Введите положительное число: '))
#     if n < 0:
# #         break
# m = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     m *= n
# print(m)

# i = 0
# while i < 10:
#     print(i)
#     i +=1
# else:
#     print('Цикл окончен, i = ', i)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print(' Внутренний цикл: j =', j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     print()
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j,'\t\t', end='')
#         j += 1
#     i += 1

# for i in 'Hello', 'red', 'black', 'yellow':
#     print(i)

# print(range(5))

# for i in range(5, 100, 5):
#     print(i, end=' ')
# print()
#
# i = 5
# while i < 100:
#     print(i, end=' ')
#     i += 5

# x = int(input('Введите целое число: '))
# for i in range(1, x+1):
#     if x % i == 0:
#         print(i, end=' ')


# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=' ')

# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('-----')

# w = int(input('Введите ширину прямоугольника: '))
# h = int(input('Введите высоту прямоугольника: '))
# for i in range(h):
#     for j in range(w):
#         print('*', end='')
#     print()

# w = int(input('Введите ширину прямоугольника: '))
# h = int(input('Введите высоту прямоугольника: '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# letter = [i for i in "Hello"]
# print(letter)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# s = []
# print(s)
# b = list()
# print(b)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)

# n = list(range(10))
# print(n)

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# n = 5
# a = [i * 3 for i in 'Hello']
# print(a)

# a = [0] * int(input('Введите количество элементов списка: '))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('-> '))
# print(a)

# a = [input('-> ')for i in range(int(input('Введите количество элементов списка: ')))]
# print(a)

# nums = [8, 3, 9, 5, 7]
#
# for i in range(len(nums)):
#     print(nums[i], end=' ')
# print()
# for i in nums:
#     print(i, end=' ')

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов списка: ')))]
# summa = 0
# for i in a:
#     if i < 0:
#         summa += i
# print('Сумма отрицательных элементов: ', summa)

# a = list(range(21, 41))
# print(a)
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         odd += 1
#     else:
#         even += i
# print('Четных: ', odd, '\nНечетных: ', even)

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = input('-> ')
#     s.append(x)
# print(s)

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3:  '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3 без остатка')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c= []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 2, 4]
# c = []
#
# if len(b) > len(a):
#     a, b = b, a
#         for i in range(len(a)):
#             c.append(a[i])
#             c.append(b[i])
#         for i in range(len(a), len(b)):
#             c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)


# n = [int(input('Количество элементов списка: '))]
# for num in range(n):
#     x = int(input('-> '))
# ind = int(input('Введите индекс: '))
# n.pop(ind)
# print(n)

# a = [1, 3, 2, 9, 7, 2, 4, 2]
# num = a.count(2)
# print(num)
# ind = a.index(9)
# print(ind)

# import random
#
# print(random.random())
# print(random.randint(2, 9))
# print(random.randrange(9))

# import random as r

# mas = [r.randint(30, 100) for i in range(10)]
# print(mas)

# lst = [4, 5, 2, 7, 4]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# s = [8, 9, 6, 4, 5, 6, 2, 4, 6, 8, 9]
# res = []
#
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
#
# print(res)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)

# lst = []
# # if len(lst) == 0:
# if not lst:
#     print('Список пуст')

from random import randint


# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print('Первый список: ', a)
# print('Второй список: ', b)
# c = a + b
# print('Третий список: ', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print('Элементы двух списков без повторения: ', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print('Список с общими элементами: ', c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# n = int(input("Размер списка: "))
# s = []
# while len(s) < n:
#     num = random.randrange(n)
#     if num not in s:
#         s.append(num)
# print(s)

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # print(m)
# # print(m[1][2])
#
# # for row in range(len(m)):
# #     for col in range(len(m[row])):
# #         print(m[row][col], end='\t')
# #     print()
#
# # for row in m:
# #     for col in row:
# #         print(col, end='\t')
# #     print()
#
# w, h = 5, 3
# # matrix = [[x * y for x in range(w)] for y in range(h)]
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y)

# w, h = 5,3
# matrix = [[randint(10, 100) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# w, h = 3, 4
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print('Количество отрицательных элементов: ')

# w = h = 6
# n = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
#
# s = []
# m = 101
# for i in range(w):
#     s.append(matrix[i][i])
#     if m > matrix[i][i]:
#         m = matrix[i][i]

#
# import math
#
# num1 = math.sqrt(2)

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime()
# print(local_time)
#
# res = time.localtime()
#
#
#
# print(time.strftime('%B %d, %Y')

# text = input('Название напоминания: ')
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)


# def hello(name):
#     print('d', name)
#
#
# hello('ira')


# def get_sum(a, b):
#     print(a + b)
#
#
# get_sum(2, 5)


# def symbol(count, a, b):
#     # print((a+b) * (count // 2) + a * (count % 2))
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#     print()
#     # print("".join([a if i % 2 == 0 else b for i in range(count)]))
#
#
# symbol(9, '-', '+')


# def check_password(password):
#     has_upper = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#
#     if len(password) >= 8 and has_upper:
#         return True
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Этот пароль надежный')
# else:
#     print('Это ненадежный пароль')

# def cube(a):
#     return a * a * a
#
#
# for i in range(1,11):
#     print(i, 'в кубе =', cube(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.insert(0, end)
#     lst.append(start)
#     return lst
#
#
# print(change([1,2,3]))
# print(change([9,12,33,54,105]))
# print(change(['s','l','o','n']))


# def get_sum(a, b, c, d):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 7))

# import time
#
# res = time.localtime()
# print(res)

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]

# lst = [10,20,30]
# tpl = (10, 20, 30)

# from random import randint
#
# s = tuple(randint(1, 30) for i in range(20))
# print(s)
#
# w = tuple(2 ** i for i in range(1,13))
# print(w)

# t1 = tuple('Hello')
# t2 = tuple('world')

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1 ) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tuple_parse(tup, num):
#     if not num in tup:
#         return tuple()
#     first = tup.index(num)
#     if not num in tup[first + 1:]:
#         return tup[first:]
#     last = tup.index(num, first + 1)
#     return tup[first:last + 1]
#
#
# print(tuple_parse((1, 2, 3), 8))
# print(tuple_parse((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(tuple_parse((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
#
#
# def tpl_sum(a, b):
#     return tuple(randint(a, b) for i in range(12))
#
#
# t1 = tpl_sum(0, 5)
# print(t1)
# t2 = tpl_sum(-5, 0)
# print(t2)
# print(t1 + t2, (t1 + t2).count(0))


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# print(t, id(t))

# a = list(range(2))
# print(a)
# print(a.__sizeof__())
# b = list(range(100))
# print(b)
# print(b.__sizeof__())


# def get_user():
#     name = 'Noy'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
# name1, age1, married1 = get_user()
# print(name1, age1, married1)

# point = (10, 20)
# match point:
#     case (0, 0):
#         print("Точка находится в координатах 0:0")
#     case (x, 0):
#         print("Точка находится в координате", x, "по оси Х и в координате 0 по оси Y")
#     case (0, y):
#         print("!!!Точка находится в координате 0 по оси Х и в координате", y, "по оси Y")
#     case (x, y):
#         print("Точка находится в координате", x, "по оси Х и в координате", y, "по оси Y")
#     case _:
#         print("Это не координаты точки")

# t = [2, 3]
# print("t =", id(t))
# print(id(t[0]))
# t[0] = 5
# print(t)
# print(id(t[0]))
# print("t =", id(t))
# a = 5
# print(id(a))

# Распаковка кортежей#
#
# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# x, y, z = t
# print(x, y, z)
# print(lst)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6))))
# print(countries)
# print()
# for country in countries:
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население =", countryPopulation)
#     for city in cities:
#         cityName, cityPopulation = city
#         print("\tГород:", cityName, "население =", cityPopulation)

# numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6 ]
# s = list({x for x in numbers if x % 2 == 0})
# print(s)

# a = 'Я обычная строка'
# b = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
#
#
# def to_set(par):
#     return set(par), len(set(par))
#
# print(to_set(a))
# print(to_set(b))


# s = {'banana', 'apple', 'orange'}
# print('apple' in s)
#
# for i in s:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# b = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# c = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
# print(b)
# print(c)
#
# # если не брать тернарное
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])

# s = {'banana', 'apple', 'orange'}
# s.add(4)
# s.remove(4)
# s.pop()
# print(s)
#
# a = {0,1,2,3}
# b = {4,3,2,1}
# c = a.union(b)
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1.union(s2, s3, s4, s5, s6, s7)
# c = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = 'Hello'
# s2 = 'How are you?'
# a = set(s1) & set(s2)
# for i in a
#     print(i, end = '')

# s1 = 'Python'
# s2 = 'Programming language'
# a = set(s1) - set(s2)
# print(a)


# drawing = {'Marina', 'Genya', 'Sveta'}
# music = {'Kostia', 'Genya', 'Ilya'}
# one_hobby = drawing ^ music
# both_hobby = drawing & music
# drawing = drawing - both_hobby
# print(one_hobby)
# print(both_hobby)
# print(drawing)

# s = frozenset([1,2,3,4,5])
# print(s)
#
# s1 = frozenset({'Hello', 'world'})
# print(s1)

# a = [1,2,3]
# d = {'one': 1, 'two': 2, 'three': 3}
# print(a[0])
# print(d['one'])

# a = [1,2,3]
# c = [1,2,3]
# b = dict(a)
# print(b)

# a = [
#     ['anna@mail.ru', 'Anna'],
#     ['ira@mail.ru', 'Ira'],
#     ['Igor@mail.ru', 'Igor'],
# ]
#
# b = dict(a)
# print(b)

# d = {i: i**2 for i in range(2,7)}
# print(d)

# d = {0: 'text', 'one': 45, (1,2.3): 'tuple', 42: [2,56,8], True: 1}
# print(d)
# # print(d[42][2])
#
# for key in d:
#     print(key, '-> ', d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# s = 1
# for i in d:
#     s *= d[i]
#
# print(s)

# d = dict()
# d[1] = input('->: ')
# d[2] = input('->: ')
# d[3] = input('->: ')
# d[4] = input('->: ')
# d = {i: input('-> ') for i in range(1,5)}
# print(d)
# dislike = int(input('Какой элемент исключить? '))
# del d[dislike]
# print(d)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ',goods[i][1] ,'шт. по ',goods[i][2],'руб', sep='')
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         qty = int(input('Количество товара: '))
#         goods[n][1] = qty
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], ' - ',goods[i][1] ,'шт. по ',goods[i][2],'руб', sep='')

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# new_d = {'name': d.pop('name'), 'salary':d.pop('salary')}
#
#
# print(d)
# print(new_d)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
#
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep='')

# sales = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4232, 'S': 6786, 'E': 4738, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3908, 'S': 3645, 'E': 8821, 'W': 2451},
# }
#
# print(sales)
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep='')
#
# person = input('Имя: ')
#
# region = input('Регион: ')
# print(sales[person][region])
# new_data = int(input('Новое значение: '))
# sales[person][region] = new_data
# print(sales[person])

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print({v : k for k, v in d.items()})
#
# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)

# one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}

# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '-> ', v1)
#     print(k2, '-> ', v2)

# pairs = [(1, 'a'), (2, 'b'),(3, 'c'), (4, 'd')]
# a,b = zip(*pairs)
# print(a)
# print(b)

# d = {'c': 3, 'a': 1, 'b': 2, 'd': 4}
# w = {k: v for k, v in d.items()}
# print(w)
# for i, j in d.items():
#     if len(d) <= 2:
#         print(i, ":", j)

# d = {'a': 1, 'b': 2, 'c': 3}
# count = 0
# for i in d:
#     print(i, ':', d[i])
#     count += 1
#     if count == 2:
#         break

# value = int(input("-> "))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# value = list(d.keys())
# print(value)
# value = list(d.values())
# print(value)
# value = list(d.items())
# print(value)


# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
#
# d = dict()
# s = None
#
# for i in a:
#     if type(i) == str:
#         d[i] = []  # d['two'] = []
#         s = i  # s = 'two'
#     else:
#         d[s].append(i)  # d['two'] = [10, 20]
#
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = dict(zip(b, a))
# print(d)


# b = [12, 1, 2]
# d = list(zip(b))
# print(d)


# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = [2.0, 4.6, 7.5]
#
# d = list(zip(a, b, c))
# print(d)


# one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# obj = {
#     'one': {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'},
#     'two': {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# }
# print(obj)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)

# one = {'apple': 0.4, 'orange': 0.35, 'pepper': 0.6}
# two = {'pepper': 0.8, 'onion': 0.55}
# print({**one, **two})


# {{'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55}}
# {'apple': 0.4, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}

# data = ['a', 'b', 'c', 'd']
#
# for i in data:
#     print(i, end=" ")
# print()
# for i in range(len(data)):
#     print(i, end=" ")
# print()
# #
# j = 1
#
# for i in data:
#     print(j, ":", i)
#     j += 1

# for j, i in enumerate(data, 100):
#     print(j, ":", i)

# n = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# for j, (i, v) in enumerate(n.items(), 100):
#     print(j, ":", i, "->", v)


# a = [1, 2, 3]
# b = [4, *a, 5, 6]
# print(b)


# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(3, 2))
# print(func(3, 4, 6, 9, 5))
# print(func())

# def to_dict(*lst):
#     return {i:i for i in lst}
#
#
# print(to_dict(1,2,3,4))
# print(to_dict('gray', (2,17), 3.11, -4))

# def to_ch(*arg):
#     return[i for i in arg if i < sum(arg)/ len(arg)]
#
#
# print(to_ch(1,2,3,4,5,6,7,8,9))
# print(to_ch(3,6,1,9,5))

# def func(a, *args):
#     return a, args
#
#
# print(func(5))

#
# def print_scores(student, *scores):
#     print('\nStudent Name: ', student, end=', scores: ')
#     a, b = None, ''
#     for score in scores:
#         a = str(score) + ', '
#         b += a
#     print(b[:-2])
#
#
# print_scores('Kate',100,95,88,92,99)
# print_scores('Rick',96,20,33,56)
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or (only_add and i % 2):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))

# def func(**date):
#     for key, value in date.items():
#         print(key, 'is', value)
#     print()
#
# func(name='Irina', surname='Sharma', age=22, phone=123456789)
# func(name='Igor', surname='Wood', email='igor@mail.ru', country='Russia',age=22, phone=9991258476)
# my_dict = {'one': 'first'}
#
#
# def db(**date):
#     # for key, value in date.items():
#     #     my_dict[key] = value
#     # return my_dict
#     my_dict.update(**date)
#
#
# print(db(k1=22, k2=31, k3=11, k4=91))
# print(db(name='Bob', age=31, weight=61, eyes_color='grey'))

# def func(*args, **data):
#     print(args[0], data)
#
# func(5,4,8,9,k1=22, k2=31, k3=11, k4=91)


# name = 'Tom'   #глобальная переменная
#
# def hi():
#     global name
#     name = 'Sam'  #локальные переменные
#     surname = 'John'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
# hi()
# bye()


# i = 5
#
# def func(arg=i):
#     print(arg)
#
# i = 6
# func()

# def add_two(a):
#     x = 2
#
#     def add_some():
#         return a + x
#
#     return add_some()
#
# print(add_two(3))

# def outer_func():
#     def inner_func():
#         print('Hello, world')
#
#     inner_func()
#
# outer_func()

# x = 25
#
# def fn():
#     global t
#     a = 30
#     t = a
#
#
# fn()
# z = x + t
# print(z)


# def func(city):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return wrap
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()

#
# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print('A = ', A(students))
# print('B = ', B(students))
# print('C = ', C(students))
# print('D = ', D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# obj1()


# Анонимные функции

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x**2+y**2)(2, 5))

# summ = lambda a, b, c=3: a + b + c
#
# print(summ(10, 20, 30))
# print(summ(10, 20))

# func = lambda *args:args
#
# print(func(1, 2, 3, 4, 5))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#      print(t('abc_'))


# def inc(n):
#     return lambda x: n + x
#
# f = inc(42)
# print(f(3))
#
# inc1 = (lambda n: lambda x: n + x)
#
# f3 = inc1(42)
# print(f3(3))
#
# def inc2(n):
#     def wrap(x):
#         return n + x
#
#     return wrap
#
# f1 = inc2(42)
# print(f1(3))

# print((lambda x: lambda y: lambda z: x + y + z)(2)(4)(6))

# players = [
#     {'name': 'Anton', 'last name': 'Birukov', 'raiting': 9},
#     {'name': 'Alex', 'last name': 'Bodnya', 'raiting': 10},
#     {'name': 'Fedor', 'last name': 'Sidorov', 'raiting': 4},
#     {'name': 'Mihail', 'last name': 'Semenov', 'raiting': 6}
# ]
#
# res = sorted(players, key = lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key = lambda item: item['raiting'])
# print(res)
#
# res = sorted(players, key = lambda item: item['raiting'], reverse = True)
# print(res)
#
# d = {'b': 15, 'a': 3, 'c': 7}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# print(dict(lst))

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(a[0](12, 3))

# a = {'one': lambda x: x - 1, 'two': lambda x: x - 3, 'three': lambda x: x}
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda : print('Понедельник'),
#     2: lambda : print('Вторник'),
#     3: lambda : print('Среда'),
#     4: lambda : print('Четверг'),
#     5: lambda : print('Пятница'),
#     6: lambda : print('Суббота'),
#     7: lambda : print('Воскресенье')
# }
#
# d[3]()

# m = lambda a, b: a if a > b else b
# print(m(2, 5))

# m = lambda a,b,c: a if a < b and a < c else b if b < c and b < a else c
# print(m(19,18,15))

# map()

# def mul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lst2 = set(map(mul, lst))
# print(lst2)

# t = (2.88, -1.75, 100.03)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)


# filter(func,iterable)

# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66,90,68,59,76,50,88,74,81,65]
# res = list(filter(lambda s: s>75, b))
# print(res)

# from random import randrange

# lst = [randint(1,40)for i in range(10)]
# print(lst)
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst2)

# nums = [45,55,60,37,100,105,220]
# res = list(filter(lambda x: x%15 == 0, nums))
# print(res)

# m = list(map(lambda x: x**2, filter(lambda x: x%2, range(10))))
# print(m)

# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am super')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
#
# @my_decorator
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# func_test()
# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# @bold
# def hello():
#     return 'text'
#
# print(hello())

# def cnt(fn):
#     count = 0
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('Вызов функции: ', count)
#     return wrap
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('Hi', arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first,second, last):
#     print('Меня зовут', first,second, last)
#
#
# print_full_name('Ирина',"Назарова")
# print_full_name("Виктор", "Федерович", "Назаров")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print(a + b)

#
# @decor("Разность:", '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#
#         return wrap
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     return 'Некорректный тип данных'
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 'Doge'))

# def multiplay(args1):
#     def wrapper(return_num):
#         def wrap(num):
#             return args1*num
#         return wrap
#     return wrapper
#
#
# @multiplay(3)
# def return_num(num):
#     return num
# print(return_num(5))

s = 5
print(s)








































































































































































































































































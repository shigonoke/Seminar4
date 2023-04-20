# Python Seminar4

# my_str = 'Hello, World!'

# print(my_str.split(' '))#split- строковый метод, разрубает строку по разделителю и
# # каждый кусочек ложит в список
# split()
# split(' ') #разделить строку по пробелу стр 7 и 8
# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()
# 1 вариант
# test_list = ("a a a b c a a d c d d").split()
# print(type(test_list))
# slovar={}
# result=None
# for i in test_list:
#     if i in slovar:
#         print(f'{i}_{slovar[i]}')
#         slovar[i] += 1
# else:
#     print(f'{i}')
#     slovar[i]=1
#2 вариант
# string = "a a a b c a a d c d d"
# my_list = string.split()
# my_dict = dict()
# for i in range(len(my_list)):
#     if my_list[i] in my_dict.keys():
#         my_dict[my_list[i]] += 1
#         my_list[i] = f"{my_list[i]}_{my_dict[my_list[i]]}"
#     else:
#         my_dict[my_list[i]] = 0
#     print(my_list)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
# text = ("She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells seashells on the sea shore I'm sure that the shells are seashore shells")

# print(len(set(text.lower().split())))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# num = int(input("Введите число:"))
# max_num = num
# while num !=0:
#     num = int(input("Введите число:"))
#     if num > max_num:
#         max_num = num
# print(max_num)
#Моржовый оператор :=
# maxx = -1
# list = []
# while (number:= int(input("Введите число"))) !=0:
#     if number > maxx:
#         maxx = number
#     print(maxx)
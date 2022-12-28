# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

import random

random.seed                                         
n = random.randint(3, 10)

list = []
for i in range(n):
    list.append(random.randint(0, 10))              
print(f'Сгенерирован список: {list}')

check_list = []
for i in list:
    if i in check_list:
        continue
    else:
        check_list.append(i)
        
print(f'Список неповторяющихся элементов: {check_list}')
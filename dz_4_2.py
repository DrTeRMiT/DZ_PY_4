# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.


def getListMult(numN):
    list = []
    listMult = [list.append(i) for i in range(1, numN+1) if numN % i == 0]
    return list


def primeNum(numN):
    primeList = []
    for i in range(2, numN):
        while numN % i == 0:
            numN /= i
            primeList.append(i)
    return primeList



numN = int(input("Введите натуральное число: "))
list1 = getListMult(numN)
print(f'Множители числа {numN} : {list1}')
list2 = primeNum(numN)

check_list = []
for i in list2:
    if i in check_list:
        continue
    else:
        check_list.append(i)

print(f'Простые множители числа {numN} :{check_list}')
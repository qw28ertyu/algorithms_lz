import random

spisok = random.sample(range(1,1000001), 100) # создаётся рандомный список из 100 элементов
print(spisok) # вывод списка 

a = int(input('введите искомый элемент: '))

#линейный список 
shetchik = 0
if a in spisok:    
    for i in range(0, len(spisok)):
        shetchik = shetchik + 1 
        if spisok[i] == a: 
            break
    print('Индекс искомого в линейном поиске :', i)
    print('Количество сравнений в линейном поиске:', shetchik)    
else :
    print('Элемент не найден в первом списке') # вывод ошибки


#бинарный поиск
spisok2 = sorted(spisok) # отсортированный заново список
print("отсортированный список для бинарного поиска: ", spisok2) # вывод отсортироанного списка

shetchik2 = 0
index = -1 #Индекс -1, так как элемент еще не найден
first = 0
last = len(spisok) - 1

b = int(input('введите искомый элемент: '))

while (first <= last) and index == -1:
    mid = (first + last)//2
    shetchik2 = shetchik2 + 1 

    if spisok[mid] == b:
            index = mid # сохраняем найденный индекс
    else :
            # если искомый элемент меньше среднего
        if b < spisok[mid]:
        # Ищем в левой половине списка
            last = mid - 1
        else:
            first = mid + 1
    if index != -1:     
        print('Количество сравнений в бинарном поиске :', shetchik2)
        print('Индекс искомого элемента в бинарном поиске :', index)

else:
    print('элемент не найден во втором списке')     # вывод ошибки
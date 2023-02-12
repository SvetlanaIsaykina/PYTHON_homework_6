#Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def chek_numbers(x, y):
    min_num = min(x, y)
    divider = 1
    for el in range(2, min_num+1):
        if x % el == 0 and y % el == 0:
            divider = el
            break
    return divider == 1

for y in range(1, 12):
    for x in range(1,y):
        if chek_numbers(x,y):
            print(f'{x}/{y}', end= ' ')
    print() 
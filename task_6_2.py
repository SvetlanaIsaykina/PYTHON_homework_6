import random 

# Задача 2. Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число. Напишите
# программу, которая определяет, есть в массиве
# последовательность из трёх элементов, совпадающая с
# введённым числом.

numbers = [random.randint(0,9) for _ in range(15)]
print(numbers)

numbers = "".join(map(str, numbers)) 
random_digit = input('Введите трёхзначное число: ')

if random_digit in numbers:
  print(f'Число {random_digit} встречается в массиве чисел')
else:
  print(f'Число {random_digit} не встречается в массиве чисел')
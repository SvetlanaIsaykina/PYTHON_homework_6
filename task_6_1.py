import random

num_n = str(random.randint(1,999))
num_nn = num_n * 2
num_nnn = num_n * 3

print(f'Число N - {num_n}')

result = int(num_n) + int(num_nn) + int(num_nnn)
print(f'Значение выражения {num_n} + {num_nn} + {num_nnn} равно {result}')
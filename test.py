number = int(init('Введите число: '))

for _ in range(10, 0, -1):
    number -= _
    print(f'Уменьшаем число {number} на {_}')

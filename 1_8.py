# Волков Владислав Станиславович
# Вариант 4
# Дан словарь с натуральными ключами {1: 'Один', 2: 'Два', 3: 'Три', 100: 'сто'}. 
# Выведите на экран сумму ключей, максимальное и минимальное значения ключей, а также их количество

dict = {1: 'Один', 2: 'Два', 3: 'Три', 100: 'Сто'}

lst = list(dict)
print('Сумма: ', sum(lst), '\nМаксимальное: ', max(lst), '\nМинимальное: ', min(lst))
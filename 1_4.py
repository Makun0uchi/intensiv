# Волков Владислав Станиславович
# Вариант 4
# Задание: Декоратор умножающий на 2 результат выполнения функции

def decorate(f):
    def wrapper(*args):
        print('Результат без декоратора: ', f(*args))
        result = f(*args) * 2
        return result
    return wrapper

@decorate
def func(value1, value2):
    return value1 + value2

print('Результат с декоратором :', func(10, 20))
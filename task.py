# Волков Владислав Станиславович
# Вариант 4
'''
Определите класс A, включающий:
строку документирования класса ''Класс A'';
метод set_a() для установки значения атрибута a;
метод get_a() для получения значения этого атрибута.

Определите класс B, включающий:
строку документирования класса ''Класс B'';
конструктор, инициализирующий атрибут данных b создаваемых экземпляров;
метод get_b() для получения значения этого атрибута.

Определите класс C, наследующий классы A (задача №2) и B (задача №3) и включающий:
строку документирования класса ''Класс C = A + B'';
конструктор, инициализирующий дополнительно атрибуты данных a и c создаваемых экземпляров;
собственные методы set_b() и set_c() для установки значений соответствующих атрибутов;
собственный метод get_c() для получения значения атрибута c

Определите класс D, включающий:
статический метод stat_print_dict, выводящий на экран словарь атрибутов переданного ему объекта класса;
метод класса cls_print_dict, выводящий на экран словарь атрибутов своего класса.
'''

class A:
    '''Класс А'''
    def set_a(self, value):
        self.a = value

    def get_a(self):
        print('a = ', self.a)

class B:
    '''Класс В'''
    def __init__(self, value):
        self.b = value

    def get_b(self):
        print('b = ', self.b)

class C(A, B):
    '''Класс С = А + В'''
    def __init__(self, value1, value2):
        self.a = value1
        self.c = value2

    def set_b(self, value):
        self.b = value

    def set_c(self):
        self.c = self.a + self.b

    def get_c(self):
        print('c = ', self.c)

class D:
    '''Класс D'''
    def __init__(self, value):
        self.d = value
    
    def stat_print_dict(self, obj):
        print(obj.__dict__)

    def cls_print_dict(self):
        print(self.__dict__)

print('class A:')
first = A()
first.set_a(20)
first.get_a()

print('class B:')
second = B(30)
second.get_b()

print('class C:')
third = C(50, 70)
third.set_b(60)
third.get_a()
third.get_b()
third.get_c() # значение атрибута с из конструктора
third.set_c() # устанавливаем значение атрибуса с как сумма атрибутов а и в
third.get_c()

print('class D:')
fourth = D(4)
fourth.cls_print_dict()
fourth.stat_print_dict(third)
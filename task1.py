# Создайте класс МояСтрока
# где будут доступны все возможности
# str и дополнительно хранится имя автора строки
# и время создания (time.time)


from datetime import datetime
import time
class MyString(str):
    """ Класс MyString где на вход поступаюе:
    value - со всеми возможностями str;
    name = имя автора строки.

    Дополнительно:
    time = время создания (time.time) """

    def __new__(cls, value: str, name: str = None):
        instance = super().__new__(cls, value)
        instance.name = name
        time.sleep(1)
        instance.time = time.ctime()
        return instance

if __name__ == '__main__':
    t = MyString("HELLO? i'm one string", 'Alex')
    t2 = MyString("HELLO? i'm two string", 'Jo')
    t3 = MyString("HELLO? i'm three string")
    st = t + t2 + t3 + 'Hero'
    print(f'{st = }')
    print(f'{t = }\t{t.name = }\t{t.time}')
    print(f'{t2 = }\t{t2.name = }\t{t2.time}')
    print(f'{t3 = }\t{t3.name = }\t{t3.time}')
    # res = t.__doc__
    # for line in res.split('\n'):
    #     print(line)
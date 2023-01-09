#импорт библиотек
import string
import random
#переменная для хранения выходной строки
s = ''
#цикл на 11 элементов
for i in range(11):
    #рандомно выбираем цифру из символов ASCII
    s += random.choice(string.ascii_letters)
print(s)
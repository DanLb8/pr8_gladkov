#импорт библиотеки
import random
#функция
def password():
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    d = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']
    g = ['1','2','3','4','5','6','7','8','9','0']
    result = ''
    for i in range(11):
        result += random.choice(a+d+g)
    return result
p = password()
print(p)

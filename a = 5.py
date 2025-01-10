# ___Задача 1___
a = 5
b = 7
summa = a + b
print(summa)

# ___Задача 2___
a = 10
b = 20
c = 30
summa = a + b + c
print(summa)

# ___Задача 3___
# 1)
count = int(input("Enter a number: ")) # функции int и input превращают строку которую ввел  пользователь в число и сначала выводят пользователю "Enter a number: "
# 2)
print("Enter a number: ")
count = int(input()) # тот же код, ничем не отличается 
# 3)
count = int(input()) # так же запрашиает у пользователя строку и превращает в число, но не пишет в начале "Enter a number:"
# 4)
count = 5 # просто присваивает переменной count значение

# ___Задача 4___ 
# функция int превращает строку в число. input запрашивает у пользователя строку, можно обойтись без этих функций

# ___Задача 5___
numbers = [5, 4, 3, 2, 1]
reversed_numbers = numbers[::-1]

# ___Задача 6___
# i в цикле это переменна которая показывает текущую итерацию
# например в цикле for i in range(5) 5 итераций, но i = 4, потому что последняя итерация будет с числом 4
# i можно заменить любой буквой или словом
# нужно обязательно писать на месте i что то, потому что нужно фиксированное значение, чтобы можно было работать с ним

# ___Задача 7___ 
count = int(input())
summa = 0
for i in range(count):
    num = int(input())
    summa = num + summa
print(summa)

# ___Задача 8___
count = int(input())
summa = 1
for i in range(count):
    num = int(input())
    summa = num * summa
print(summa)
# код отличается от предыдущего тем, что в 51 строке стоит знак умножения и сумма изначально равна 1, тк на 0 умножать нельзя

# ___Задача 9___ 
name = "Grisha"
surname = "Fedorov"
message_to_person = name + surname + "Hello!"
print(message_to_person)
# чтобы исправить проблему того, что имя и фамилия пишутся слитно нужно написать между ними пробел " "
name = "Grisha"
surname = "Fedorov"
message_to_person = name + " " + surname + " " + "Hello!"
print(message_to_person)

# ___Задача 10___
count = int(input("Enter a count: "))
message = ""
for i in range(count):
    str = input("Enter a string: ")
    message += str + " "
print(message)
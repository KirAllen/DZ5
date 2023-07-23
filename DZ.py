
# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

file = input("Path: ")

def file_path(path: str) -> tuple:
    *path, name= path.split("\\")
    res = ['/'.join(path), name.split('.')[0], name.split('.')[1]]
    return (tuple(res))

print(file_path(file))


# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида «10.25%». В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии




name = ["Ivan", "Petr", "Maxim"]
stavka = [100_555, 200_111, 90_344]
percent = ["10.25%", "11.12%", "25.0%"]
dictionary = {name: (int(stavka) * float(percent[:-1])/100) for name,stavka,percent in zip(name, stavka, percent)}

print(dictionary)


# Fibonacci

num = int(input("Введите число: "))

def fibonacci(n):
    number1 = 0
    number2 = 1
    for i in range(0, n):
        number1 += number2
        number2 = number1-number2
        yield number1

print("0 = 0")
for i, num in enumerate(fibonacci(num), start=0):
    print(f"{i+1} = {num}")
# 1.task
# Создайте список из 6 элементов, замените первый элемент на новый и выведите изменённый список.
items = [10, 20, 30, 40, 50, 60]
items[0] = 100
print(items)

# 2.task
# Напишите программу, которая удаляет последний элемент из списка и выводит изменённый список.
items = [1, 2, 3, 4, 5]
items.pop()
print(items)

# 3.task
# Создайте список из 5 чисел и найдите сумму всех элементов списка.
numbers = [1, 2, 3, 4, 5]
total_sum = 0
for num in numbers:
    total_sum += num
print(total_sum)

# 4.task
# Напишите программу, которая создает список из 3 строк и объединяет их в одну строку через пробел.
strings = ["Hello", "world", "Python"]
result = ""
for s in strings:
    if result:
        result += " "
    result += s
print(result)

# 5.task
# Создайте список из 4 чисел и найдите произведение всех элементов списка, при этом в цикле проверяя не равняется ли элемент 0, если нет то продолжить умножение.
numbers = [2, 0, 3, 4]
product = 1

for number in numbers:
    if number != 0:
        product *= number

print(product)
# 6.task

# 7.task

# 8.task

# 9.task

# 10.task

# 11.task

# 12.task

# 13.task

# 14.task

# 15.task

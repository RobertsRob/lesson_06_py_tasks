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
# Создайте список из 7 чисел и найдите максимальный элемент без использования встроенных функций.
numbers = [10, 20, 30, 40, 50, 60, 70]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print(max_value)

# 7.task
# Напишите программу, которая создает список из 5 строк и удаляет строку по индексу, введенному пользователем, при этом проверая ведёный индекс на достоверность. 
strings = ["a", "b", "c", "d", "e"]
index = int(input("Enter index to remove: "))
if 0 <= index < len(strings):
    del strings[index]
print(strings)

# 8.task
# Создайте список из 5 чисел и найдите их среднее значение.
numbers = [10, 20, 30, 40, 50]
total_sum = 0
for num in numbers:
    total_sum += num
average = total_sum / len(numbers)
print(average)

# 9.task
# Напишите программу, которая меняет порядок элементов списка на противоположный.
# good:
numbers = [1, 2, 3, 4, 5, 6]
reversed_list = []
for num in numbers:
    reversed_list.insert(0, num)
print(reversed_list)

# better:
numbers = [1, 2, 3, 4, 5, 6]
reversed_numbers = numbers[::-1]
print(reversed_numbers)

# 10.task
# Создайте список из 4 строк, и найдите строку, которая имеет наибольшую длину.
strings = ["one", "three", "fourteen", "six"]
longest = strings[0]
for s in strings:
    if len(s) > len(longest):
        longest = s
print(longest)

# 11.task
# Напишите программу, которая создает список из 5 чисел и удаляет все числа, которые меньше среднего значения.
numbers = [10, 20, 30, 40, 50]

total_sum = 0
for num in numbers:
    total_sum += num
average = total_sum / len(numbers)

filtered_list = []
for num in numbers:
    if num >= average:
        filtered_list.append(num)
print(filtered_list)

# 12.task
# Создайте список из 5 элементов и найдите второй по величине элемент, не используя встроенные функции.
numbers = [10, 20, 30, 40, 50]
first_max = second_max = float('-inf')
for num in numbers:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        second_max = num
print(second_max)

# 13.task
# Создайте список из 5 чисел и создайте новый список, который содержит только те числа, которые являются четными из первого списка.
numbers = [1, 2, 3, 4, 5]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(evens)

# 14.task
# Напишите программу, которая создает список из 5 чисел и заменяет все отрицательные числа на их абсолютные значения.
numbers = [-4, 5, -2, -7, 9]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = -numbers[i]
print(numbers)

# 15.task
# Напишите программу, которая создает список из 5 чисел и сортирует его в порядке возрастания.
numbers = [34, 7, 23, 32, 5]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print(numbers)

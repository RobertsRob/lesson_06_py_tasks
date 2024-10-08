# 1.task
# Создайте список из 6 чисел и отсортируйте его в порядке убывания с использованием метода sort.
numbers = [5, 2, 9, 1, 7, 6]
numbers.sort(reverse=True)
print(numbers)

# 2.task
# Создайте список из 5 чисел и найдите индекс максимального элемента, используя функции max и index.
numbers = [5, 8, 2, 10, 3]
max_value = max(numbers)
index = numbers.index(max_value)
print(index)

# 3.task
# Напишите программу, которая создает список из 5 чисел и удаляет последний элемент, используя оператор del.
numbers = [12, 7, 9, 3, 15]
del numbers[-1]
print(numbers)

# 4.task
# Напишите программу, которая создает список из 5 чисел и копирует его с использованием метода copy, затем удаляет первый элемент из копии и выводит оба списка.
numbers = [11, 22, 33, 44, 55]
numbers_copy = numbers.copy()
del numbers_copy[0]
print("Original list:", numbers)
print("Modified copy:", numbers_copy)

# 5.task
# Создайте список из 4 строк и найдите минимальную строку (в алфавитном порядке) с использованием функции min.
strings = ["banana", "apple", "cherry", "date"]
min_string = min(strings)
print(min_string)

# 6.task
# Создайте список из 6 чисел, найдите максимальный элемент, затем замените его на 0 и выведите обновленный список.
numbers = [14, 7, 25, 3, 18, 10]
max_value = max(numbers)
index = numbers.index(max_value)
numbers[index] = 0
print(numbers)

# 7.task
# Напишите программу, которая создает список из 5 строк, сортирует его по длине строк, а затем удаляет самую короткую строку.
strings = ["elephant", "cat", "hippopotamus", "dog", "mouse"]
strings.sort(key=len)
del strings[0]
print(strings)

# 8.task
# Создайте список из 7 чисел. Найдите минимальный элемент и замените все элементы списка, которые равны минимальному, на его двойное значение.
numbers = [4, 6, 8, 4, 9, 4, 7]
min_value = min(numbers)
for i in range(len(numbers)):
    if numbers[i] == min_value:
        numbers[i] = min_value * 2
print(numbers)

# 9.task
# Напишите программу, которая создает список из 6 чисел и заменяет все нечетные числа на их кубы, а затем сортирует список по возрастанию.
numbers = [2, 3, 7, 6, 9, 12]
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] = numbers[i] ** 3
numbers.sort()
print(numbers)

# 10.task
# Напишите программу, которая создает список из 6 чисел, сортирует его по возрастанию, а затем заменяет каждый второй элемент на его половину.
numbers = [5, 15, 10, 20, 25, 30]
numbers.sort()
for i in range(1, len(numbers), 2):
    numbers[i] /= 2
print(numbers)

# 11.task
# Создайте список из 8 чисел. Найдите все числа, которые делятся одновременно на 3 и на 5, и отсортируйте их по возрастанию. Выведите полученный отсортированный список.
numbers = [15, 30, 22, 45, 12, 18, 55, 60]
filtered_numbers = [num for num in numbers if num % 3 == 0 and num % 5 == 0]
filtered_numbers.sort()
print(filtered_numbers)

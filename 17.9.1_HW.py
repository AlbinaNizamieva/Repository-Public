def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


raw_array = input('Введите несколько чисел через пробел: ') # 1 3 8 6 5 9 7 4 2 56 9 5 3 1 78 5
array_listed = []
element = 0

try:
    array_listed = list(int(i) for i in raw_array.split())
    element = int(input('Какое число Вы ищите? '))
except ValueError:
    print('Необходимо указать только числа')

array_listed.sort()
print(array_listed)
index = binary_search(array_listed, element, 0, len(array_listed))
print(f'Индекс искомого элемента - {index}')

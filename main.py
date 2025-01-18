from random import randint


# Быстрая сортировка
def quick_sort(list_to_sort: list[int]) -> list[int]:
    if len(list_to_sort) < 2:
        return list_to_sort

    element: int = list_to_sort[0]
    first_part: list[int] = [n for n in list_to_sort if n < element]
    middle_part: list[int] = [n for n in list_to_sort if n == element]
    last_part: list[int] = [n for n in list_to_sort if n > element]

    return quick_sort(first_part) + middle_part + quick_sort(last_part)


# Сортировка выбором
def selection_sort(list_to_sort: list[int]) -> list[int]:
    for n in range(len(list_to_sort)):

        first_value: int = list_to_sort[n]
        min_value: int = min(list_to_sort[n:])
        min_index: int = list_to_sort[n:].index(min_value) + n

        if n == min_index:
            continue

        list_to_sort[n]: int = min_value
        list_to_sort[min_index]: int = first_value

    return list_to_sort


# Сортировка вставками
def insertion_sort(list_to_sort: list[int]) -> list[int]:
    left: list[int] = []
    middle: list[int] = []
    right: list[int] = []

    for n in range(len(list_to_sort)):

        element: int = list_to_sort[n]

        left: list[int] = [n for n in list_to_sort if n < element]
        middle: list[int] = [n for n in list_to_sort if n == element]
        right: list[int] = [n for n in list_to_sort if n > element]

    return left + middle + right


if __name__ == '__main__':
    rand_list: list[int] = [randint(-20, 20) for _ in range(20)]
    print(f'Список для сортировки: {rand_list}\n')
    print('-' * 110)
    print('Быстрая сортировка')
    print('-' * 110)
    print(f'Отсортированный список: {quick_sort(rand_list)}\n')

    print('-' * 110)
    print('Сортировка выбором')
    print('-' * 110)
    print(f'Отсортированный список: {selection_sort(rand_list)}\n')

    print('-' * 110)
    print('Сортировка вставками')
    print('-' * 110)
    print(f'Отсортированный список: {insertion_sort(rand_list)}\n')
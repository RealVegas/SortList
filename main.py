from random import randint


if __name__ == '__main__':
    rand_list: list[int] = [randint(-20, 20) for _ in range(20)]
    print(f'Список для сортировки: {rand_list}')
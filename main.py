import random


class Apple_tree:
    tree_num = 10
    tree_list = []
    fruits_list_quant = [random.randint(40, 50) for _ in range(tree_num)]
    fruits_weight = [random.randint(150, 180) for _ in range(tree_num)]
    # Произвели сбор плодов
    for i in range(tree_num):
        tree_list.append({'tree_id': i, 'fruits_quant': fruits_list_quant[i], 'fruits_weight': fruits_weight[i]})
    # Посчитали общее кол-во и вес
    fruits_total_quant = sum(i['fruits_quant'] for i in tree_list)
    fruits_total_weight = sum(i['fruits_weight'] for i in tree_list)


class Pear_tree:
    tree_num = 15
    tree_list = []
    fruits_list_quant = [random.randint(0, 20) for _ in range(tree_num)]
    fruits_weight = [random.randint(130, 170) for _ in range(tree_num)]
    # Произвели сбор плодов
    for i in range(tree_num):
        tree_list.append({'tree_id': i, 'fruits_quant': fruits_list_quant[i], 'fruits_weight': fruits_weight[i]})
    # Посчитали общее кол-во и вес
    fruits_total_quant = sum(i['fruits_quant'] for i in tree_list)
    fruits_total_weight = sum(i['fruits_weight'] for i in tree_list)


# Добавили деревья в сад
garden = [Apple_tree.tree_list, Pear_tree.tree_list]
# Вывели на экран общее кол-во собранных фруктов каждого вида
print(f'Кол-во собранных плодов с яблони: {Apple_tree.fruits_total_weight}')
print(f'Кол-во собранных плодов груш: {Pear_tree.fruits_total_weight}')

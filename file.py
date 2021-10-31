import os
from pprint import pprint

with open('recipes.txt',encoding='utf-8') as file:
    cook_book = {}
    for dish in file:
        dish_name = dish.strip()
        counter = int(file.readline().strip())
        temp_data = []
        for id in range(counter):
            name, quantity, measure= file.readline().strip().split('|')
            temp_data.append({'ingredient_name': name, 'quantity': int(quantity), 'measure': measure})
        cook_book[dish_name] = temp_data
        file.readline()

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish_id in dishes:
        # pprint(cook_book[dish_id])
        # print(dish_id)
        for ing in cook_book[dish_id]:
            if shopping_list == {}:
                shopping_list[ing['ingredient_name']] = {'measure':ing['measure'],'quantity':ing['quantity']*person_count}
                # print('Самое первая запись',shopping_list)
            elif ing['ingredient_name'] in shopping_list:
                # print('уже есть')
                tmp = shopping_list[ing['ingredient_name']]
                # print(tmp)
                tmp.update(quantity=tmp['quantity'] + ing['quantity']*person_count)
                # print(tmp)
                # print(ing['ingredient_name'])
                shopping_list[ing['ingredient_name']] = tmp
                # {'measure':ing['measure'],'quantity':ing['quantity']*person_count})
            else:
                # print("добавим еще")
                shopping_list[ing['ingredient_name']] = {'measure':ing['measure'],'quantity':ing['quantity']*person_count}
                # print(shopping_list)
    return shopping_list


zakaz = get_shop_list_by_dishes(['Омлет','Омлет', 'Омлет', 'Фахитос'], 4)
pprint(zakaz)










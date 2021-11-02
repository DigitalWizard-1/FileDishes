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

def add_product(list_product,product,num):
    list_product[product['ingredient_name']] = {'measure': product['measure'], 'quantity': product['quantity'] * num}

def add_products(list_product,product,num):
    tmp = list_product[product['ingredient_name']]
    tmp.update(quantity=tmp['quantity'] + product['quantity'] * num)
    list_product[product['ingredient_name']] = tmp

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for dish_id in dishes:
        for ing in cook_book[dish_id]:
            if shopping_list == {}:
                add_product(shopping_list,ing,person_count)
            elif ing['ingredient_name'] in shopping_list:
                add_products(shopping_list,ing,person_count)
            else:
                add_product(shopping_list,ing,person_count)
    return shopping_list

zakaz = get_shop_list_by_dishes(['Омлет','Омлет', 'Омлет', 'Фахитос'], 4)
pprint(zakaz)










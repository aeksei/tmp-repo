shopping_list = [
    {"стоимость": 1000, "скидка": True},
    {"стоимость": 500, "скидка": False},
    {"стоимость": 750, "скидка": True},
    {"стоимость": 300, "скидка": False}
]

sum_coast = 0  # Сумма товаров со скидкой

for dict_item in shopping_list:
    if dict_item["скидка"]:
        coast = dict_item["стоимость"]
        sum_coast += coast

print(sum_coast)

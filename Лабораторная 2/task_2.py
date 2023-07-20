shopping_list = [
    "яблоко", "молоко", "хлеб", "яблоко", "масло", "яйца", "молоко"
]

# ключ - товар, значение - кол-во в корзине
dict_item = {}  # пустой словарь
for item in shopping_list:
    if item not in dict_item:  # Если встретил товар в первый раз
        dict_item[item] = 1  # Количество встреч 1 (в первый раз)
    else:  # Если встретил товар повторно
        dict_item[item] += 1

print(dict_item)

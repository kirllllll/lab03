def find_i(items_list, item):
    for index, i in enumerate(items_list):
        if item in items_list: #Не понятно почему не выдергивает индексы, хотя пару значений находит
            return index
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_i(items_list, find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

'''
Ответ следующий:
Первое вхождение товара 'банан' имеет индекс 0.
Первое вхождение товара 'груша' имеет индекс 0.
Товар 'персик' не найден в списке.
'''


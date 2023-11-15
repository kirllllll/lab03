def find_i(items_list, item):
#Конструкция try-except для обработки ошибок
    try:
        i = items_list.index(item)
        return i
    except ValueError: #Если будет данная ошибка, то будет выполнен блок except
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_i(items_list, find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

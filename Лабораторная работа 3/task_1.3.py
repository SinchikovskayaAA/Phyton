# TODO Напишите функцию для поиска индекса товара
def find(item_list, item):
    index = 0
    for i_item in item_list:
        index += 1
        if item == i_item:
            return index - 1
        if index == len(item_list) - 1:
            return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

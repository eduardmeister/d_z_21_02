from data.cls_abs_storage import Storage


class BaseStorage(Storage):

    def __init__(self, items, capacity):
        self._items = items
        self.capacity = capacity

    def add(self, item, value):
        """увеличивает запас items"""
        if self.get_free_space() < value:
            raise "Cвободное место закончилось"

        if self.get_items.get(item):
            self._items[item] += value
        else:
            self._items[item] = value

    def remove(self, item, value):
        """уменьшает запас items"""
        if not self.get_items.get(item):
            raise "Нет такого товара"
        if self.get_items.get(item) < value:
            raise "Не хватает товара, попробуйте заказать меньше"

        self._items[item] -= value

        if self.get_items.get(item) == 0:
            del self._items[item]

    def get_free_space(self):
        """Вернуть количество свободных мест"""
        return self.capacity - sum(self.get_items.values())

    @property
    def get_items(self):
        """Возвращает содержание склада в словаре {товар: количество}"""
        return self._items

    def get_unique_items_count(self):
        """Возвращает количество уникальных товаров"""
        return len(self.get_items.keys())

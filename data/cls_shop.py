from data.cls_basestorage import BaseStorage


class Shop(BaseStorage):
    def __init__(self, items, capacity):
        super().__init__(items, capacity)
        self.capacity = 20

    def add(self, item, value):
        """увеличивает запас items"""

        if not self._items.get(item) and self.get_unique_items_count() == 5:
            raise "Hе больше 5 разных товаров"
        super().add(item, value)



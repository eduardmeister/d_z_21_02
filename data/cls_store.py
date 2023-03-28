from data.cls_basestorage import BaseStorage


class Store(BaseStorage):

    def __init__(self, items, capacity):
        super().__init__(items, capacity)
        self.capacity = 100


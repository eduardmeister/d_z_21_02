from abc import ABC, abstractmethod


class Storage(ABC):

    @abstractmethod
    def add(self, item, value):
        """увеличивает запас items"""
        pass

    @abstractmethod
    def remove(self, item, value):
        """уменьшает запас items"""
        pass

    @abstractmethod
    def get_free_space(self):
        """Вернуть количество свободных мест"""
        pass

    @abstractmethod
    def get_items(self):
        """Возвращает содержание склада в словаре {товар: количество}"""
        pass

    @abstractmethod
    def get_unique_items_count(self):
        """Возвращает количество уникальных товаров"""
        pass

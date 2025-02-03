from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для класса Product"""
    @abstractmethod
    def new_product(self, *args, **kwargs):
        pass

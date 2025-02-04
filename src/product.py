from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для представления продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Инициализация экземпляра класса продуктов. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        super().__init__()

    @property
    def price(self):
        """Геттер возвращает приватный атрибут объекта __price"""
        return self.__price

    @price.setter
    def price(self, price):
        """Сеттер принимает новую цену и присваивает ее значение приватному атрибуту объекта __price,
        или если цена некорректна, выводит сообщение о некорректном вводе"""
        if price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product: dict[str, Any]):
        """Метод принимает атрибут product в виде словаря и возвращает объект класса"""
        name = product['name']
        description = product['description']
        price = product['price']
        quantity = product['quantity']
        return cls(name, description, price, quantity)

    def __add__(self, other):
        """Магический метод, который складывает два объекта по цене общего количества на складе"""
        if type(self) is type(other):  # Проверка на то, что объекты одного типа (класса)
            total_price_self = self.__price * self.quantity
            total_price_other = other.__price * other.quantity
            return total_price_self + total_price_other
        raise TypeError

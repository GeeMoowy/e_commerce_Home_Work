from typing import Any


class Product:
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
        self.quantity = quantity

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

    @classmethod
    def new_product(cls, product: dict[str, Any]):
        """Метод принимает атрибут product в виде словаря и возвращает объект класса"""
        name = product['name']
        description = product['description']
        price = product['price']
        quantity = product['quantity']
        return cls(name, description, price, quantity)

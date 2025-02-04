from functools import total_ordering

from src.product import Product


class Category:
    """Класс для представления категории товаров"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация экземпляра класса категории товара. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        """Геттер возвращает приватный атрибут __products"""
        return self.__products

    @property
    def products_str(self):
        """Геттер возвращает все товары в приватном списке объекта в виде строки"""
        return '\n'.join(str(product) for product in self.__products)

    def __str__(self):
        total_number_of_products = 0
        for product in self.__products:
            total_number_of_products += product.quantity
        return f"{self.name}, количество продуктов: {total_number_of_products} шт."

    def add_product(self, product: Product):
        """Метод добавляет товары в приватный атрибут self.__products"""
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        Category.product_count += 1

    def middle_price(self):
        total_amount = 0
        for product in self.__products:
            total_amount += product.price * product.quantity
        if len(self.__products) == 0:
            return 0
        else:
            result = total_amount / len(self.__products)
            return result

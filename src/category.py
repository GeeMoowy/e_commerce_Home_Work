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
        all_products_str = ''
        for product in self.__products:
            all_products_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return all_products_str

    def __str__(self):
        total_number_of_products = 0
        for product in self.__products:
            total_number_of_products += product.quantity
        return f"{self.name}, количество продуктов: {total_number_of_products} шт."


    def add_product(self, product: Product):
        """Метод добавляет товары в приватный атрибут self.__products"""
        self.__products.append(product)
        Category.product_count += 1

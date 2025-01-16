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
        return self.__products

    @property
    def products_str(self):
        product_str = ''
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str

    def add_product(self, product: Product):
        """Метод добавляет товары в приватный атрибут self.__products"""
        self.__products.append(product)
        Category.product_count += 1

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product(
        'LG 100',
        'Телевизор с диагональю "55',
        57900.50,
        2
    )


@pytest.fixture
def my_category():
    return Category(
        'Телевизоры',
        'Телевизоры с большой диагональю',
        [
            Product('LG 200', 'Плазменные телевизоры', '24000', 5),
            Product('Samsung X5', 'Плазменные телевизоры', '25500', 3)
            ]
    )

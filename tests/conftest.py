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
def product_1():
    return Product(
        'Samsung K20',
        'Телевизор с диагональю "60',
        83000.50,
        4
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


@pytest.fixture
def negative_price():
    return -66


@pytest.fixture
def correct_price():
    return 15000


@pytest.fixture
def product_in_dict():
    return {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }

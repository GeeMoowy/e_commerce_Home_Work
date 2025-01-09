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
        ['LG 100', 'Samsung X5', 'DEXP 5']
    )

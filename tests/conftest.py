import pytest
from src.product import Product


@pytest.fixture
def product():
    return Product(
        'LG 100',
        'Телевизор с диагональю "55',
        57900.50,
        2
    )

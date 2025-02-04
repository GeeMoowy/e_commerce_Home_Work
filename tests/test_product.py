import pytest
from src.product import Product


def test_product_init(product):
    assert product.name == 'LG 100'
    assert product.description == 'Телевизор с диагональю "55'
    assert product.price == 57900.50
    assert product.quantity == 2


def test_new_product(product_in_dict):
    product1 = Product.new_product(product_in_dict)
    assert product1.name == "Samsung Galaxy C23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_correct_price(product, correct_price):
    product.price = correct_price
    assert product.price == correct_price


def test_wrong_price(capsys, product, negative_price):
    product.price = negative_price
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == ('Цена не должна быть нулевая или отрицательная')


def test_add_(product, product_1):
    assert product + product_1 == 447803


def test_add_type_error(smartphone1, grass_test):
    with pytest.raises(TypeError):
        smartphone1 + grass_test


def test_init_zero_quantity():
    with pytest.raises(ValueError):
        Product(
            'Samsung K20',
            'Телевизор с диагональю "60',
            83000.50,
            0
        )

import pytest

from src.category import Category


def test_category_init(my_category):
    assert my_category.name == 'Телевизоры'
    assert my_category.description == 'Телевизоры с большой диагональю'
    assert len(my_category.products) == 2

    assert Category.product_count == 2
    assert Category.category_count == 1


def test_product_str_property(my_category):
    assert my_category.products_str == 'LG 200, 24000 руб. Остаток: 5 шт.\nSamsung X5, 25500 руб. Остаток: 3 шт.'


def test_add_product(my_category, product):
    assert len(my_category.products) == 2
    my_category.add_product(product)
    assert len(my_category.products) == 3


def test_str_method(my_category):
    assert str(my_category) == 'Телевизоры, количество продуктов: 8 шт.'


def test_add_product_type_error(my_category):
    wrong_product = 'Не продукт'
    with pytest.raises(TypeError):
        my_category.add_product(wrong_product)


def test_middle_price(my_category):
    assert my_category.middle_price() == 98250.0


def test_middle_price_product_zero(my_category_product_empty):
    assert my_category_product_empty.middle_price() == 0

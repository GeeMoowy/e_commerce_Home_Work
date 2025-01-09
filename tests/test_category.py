from src.category import Category


def test_category_init(my_category):
    assert my_category.name == 'Телевизоры'
    assert my_category.description == 'Телевизоры с большой диагональю'
    assert my_category.products == ['LG 100', 'Samsung X5', 'DEXP 5']
    assert len(my_category.products) == 3

    assert Category.product_count == 3
    assert Category.category_count == 1

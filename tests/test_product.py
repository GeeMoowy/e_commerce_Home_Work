
def test_product_init(product):
    assert product.name == 'LG 100'
    assert product.description == 'Телевизор с диагональю "55'
    assert product.price == 57900.50
    assert product.quantity == 2
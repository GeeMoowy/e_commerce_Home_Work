from src.product import Product


def test_print_mixin(capsys):
    Product('Lg', 'Телевизор черный, плазменный', 57000, 5)
    message = capsys.readouterr()
    assert message.out.strip() == 'Product(Lg, Телевизор черный, плазменный, 57000, 5)'

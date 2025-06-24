from src.product import Product


def test_product_init(product_first):
    assert product_first.name == "Samsung Galaxy C23 Ultra"
    assert product_first.description == "256GB, Серый цвет, 200MP камера"
    assert product_first.quantity == 5


def test_new_product():
    str_new_product = {"name": "Samsung Galaxy C23 Ultra",
                       "description": "256GB, Серый цвет, 200MP камера",
                       "price": 180000.0,
                       "quantity": 5}
    class_product = Product.new_product(str_new_product)
    assert class_product.name == "Samsung Galaxy C23 Ultra"
    assert class_product.description == "256GB, Серый цвет, 200MP камера"
    assert class_product.quantity == 5


def test_price(product_first):
    price = product_first.price
    assert price == 180000.0



from src.category import Category
from src.product import Product


def test_category_init(category_first):
    Category.category_count = 0  # Сбрасываем счётчик перед тестом
    Category.product_count = 0
    assert category_first.name == "Телевизоры"
    assert (
        category_first.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )


def test_category_count(category_first):
    assert category_first.category_count == 1
    assert category_first.product_count == 2


def test_add_product():
    category_second =Category(
        name="Тест",
        description="Тест",
        products=[
            Product(
                name='Тест 1',
                description="Тест",
                price=123000.0,
                quantity=6,
            ),
            Product(
                name="Тест 2",
                description="Тест",
                price=210000.0,
                quantity=8,
            ),
        ],
    )
    product_first = Product(
                name="Тест 2",
                description="Тест",
                price=210000.0,
                quantity=8,
            )
    assert category_second.product_count == 2
    category_second.add_product(product_first)
    assert category_second.product_count == 3


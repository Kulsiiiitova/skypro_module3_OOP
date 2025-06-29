import pytest

from src.category import Category
from src.product import Product


@pytest.fixture()
def product_first():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture()
def product_second():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=100000,
        quantity=5,
    )


@pytest.fixture()
def product_third():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=0,
        quantity=5,
    )


@pytest.fixture()
def category_first():
    Category.category_count = 0  # Сбрасываем счетчики перед созданием
    Category.product_count = 0
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[
            Product(
                name='"55" QLED 4K',
                description="Фоновая подсветка",
                price=123000.0,
                quantity=7,
            ),
            Product(
                name="Iphone 15",
                description="512GB, Gray space",
                price=210000.0,
                quantity=8,
            ),
        ],
    )


@pytest.fixture()
def category_second():
    Category.category_count = 0  # Сбрасываем счетчики перед созданием
    Category.product_count = 0
    return Category(
        name="Тест",
        description="Тест",
        products=[
            Product(
                name="Тест 1",
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

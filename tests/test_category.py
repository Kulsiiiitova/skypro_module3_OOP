from src.category import Category


def test_category_init(category):
    Category.category_count = 0  # Сбрасываем счётчик перед тестом
    Category.product_count = 0
    assert category.name == "Телевизоры"
    assert (
        category.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category.products) == 2


def test_category_count(category):
    assert category.category_count == 1
    assert category.product_count == 2

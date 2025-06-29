from category import Category
from product import Product

class ProductIterator:
    def __init__(self, category):
        self.category = category
        self.index = 0
    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    category = Category(
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

    iterator = ProductIterator(category)

    for product in iterator:
        print(product)

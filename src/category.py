from src.product import Product


class Category:
    """Класс, описывающий катерогиии товара"""

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products) if products else 0

    def add_product(self, products: Product):
        if products not in self.__products:
            self.__products.append(products)
            Category.product_count += 1





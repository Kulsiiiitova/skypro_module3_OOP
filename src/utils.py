import json
import os

from category import Category
from product import Product


def read_json(path: str) -> list:
    """Функция, которая загружает даннфе из json-файла и создает объекты класса"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as f:
        data = json.load(f)
    return data


def create_objects_from_json(data: list):
    category = []
    for i in data:
        products = []
        for product in i["products"]:
            products.append(Product(**product))
        i["products"] = products
        category.append(Category(**i))
    return category


# if __name__ == "__main__":
#     raw_data = read_json("data/products.json")
#     print(create_objects_from_json(raw_data))

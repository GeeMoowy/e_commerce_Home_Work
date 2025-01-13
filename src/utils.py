import json
import os

from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """Функция читает данные из json файла и преобразует их в словарь"""
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as file:
        products_dict = json.load(file)
    return products_dict


def create_obj_from_json(json_data: dict):
    """Создание экземпляров класса из json-файла"""
    categories = []
    for my_category in json_data:
        products = []
        for product in my_category['products']:
            products.append(Product(**product))
        my_category['products'] = products
        categories.append(Category(**my_category))
    return categories

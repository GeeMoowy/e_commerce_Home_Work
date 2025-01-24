from src.category import Category


class IterationProducts:
    """Вспомогательный класс для итерации по продуктам в категории"""
    category: Category

    def __init__(self, obj_category):
        """Конструктор для создания объекта класса IterationProducts"""
        self.obj_category = obj_category
        self.stop = len(self.obj_category.products)

    def __iter__(self):
        """Определяем итератор"""
        self.prod_index = -1
        return self

    def __next__(self):
        """Метод возвращает следующий элемент списка товаров в объекте категории"""
        self.prod_index += 1
        if self.prod_index < self.stop:
            return self.obj_category.products[self.prod_index]
        else:
            raise StopIteration

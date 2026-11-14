from abc import ABC, abstractmethod


class PrintedEdition(ABC):
    """Абстрактное печатное издание."""

    def __init__(self, title: str, pages: int, price: float):
        self.title = title
        self.pages = pages
        self.price = price

    @property
    def title(self) -> str:
        """Название издания."""
        return self.__title

    @title.setter
    def title(self, value: str):
        if not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("Название должно быть строкой длиной не менее 2 символов")
        self.__title = value.strip()

    @property
    def pages(self) -> int:
        """Количество страниц."""
        return self.__pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом")
        if not (1 <= value <= 10000):
            raise ValueError("Количество страниц должно быть от 1 до 10000")
        self.__pages = value

    @property
    def price(self) -> float:
        """Цена, руб."""
        return self.__price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise ValueError("Цена должна быть числом")
        if value < 0:
            raise ValueError("Цена должна быть неотрицательной")
        self.__price = float(value)

    @abstractmethod
    def get_category(self) -> str:
        """Категория издания."""
        pass

    @abstractmethod
    def illustrations_percent(self) -> int:
        """Процент страниц, занятых иллюстрациями."""
        pass

    def characters_count(self) -> int:
        """Количество печатных знаков (текст без иллюстраций)."""
        text_pages = self.pages * (100 - self.illustrations_percent()) / 100
        return int(text_pages * 1800)

    def is_periodical(self) -> bool:
        """Проверка на периодичность. По умолчанию — непериодическое."""
        return False

    def get_info(self) -> str:
        """Характеристики экземпляра."""
        periodical = "периодическое" if self.is_periodical() else "непериодическое"
        return (
            f"{self.__class__.__name__}: «{self.title}»\n"
            f"  Страниц: {self.pages}, цена: {self.price:.2f} руб.\n"
            f"  Категория: {self.get_category()}\n"
            f"  Иллюстрации: {self.illustrations_percent()}% страниц\n"
            f"  Печатных знаков: {self.characters_count()}\n"
            f"  Тип: {periodical}"
        )

    def __str__(self) -> str:
        return self.get_info()
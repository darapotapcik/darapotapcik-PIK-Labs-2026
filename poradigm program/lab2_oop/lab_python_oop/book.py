from .printed_edition import PrintedEdition


class Book(PrintedEdition):
    """Книга: непериодическое издание."""

    def __init__(self, title: str, pages: int, price: float, author: str):
        super().__init__(title, pages, price)
        self.author = author

    @property
    def author(self) -> str:
        """Автор книги."""
        return self.__author

    @author.setter
    def author(self, value: str):
        if not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("Имя автора должно быть строкой длиной не менее 2 символов")
        self.__author = value.strip()

    def get_category(self) -> str:
        return "Книга"

    def illustrations_percent(self) -> int:
        return 15
    # is_periodical() НЕ переопределяем — наследуется от PrintedEdition (False)

    def get_info(self) -> str:
        base = super().get_info()
        return base + f"\n  Автор: {self.author}"
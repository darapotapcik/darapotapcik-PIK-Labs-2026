from .printed_edition import PrintedEdition


class Textbook(PrintedEdition):
    """Учебник: непериодическое издание с предметом."""

    def __init__(self, title: str, pages: int, price: float, subject: str):
        super().__init__(title, pages, price)
        self.subject = subject

    @property
    def subject(self) -> str:
        """Учебный предмет."""
        return self.__subject

    @subject.setter
    def subject(self, value: str):
        if not isinstance(value, str) or len(value.strip()) < 2:
            raise ValueError("Предмет должен быть строкой длиной не менее 2 символов")
        self.__subject = value.strip()

    def get_category(self) -> str:
        return "Учебник"

    def illustrations_percent(self) -> int:
        return 25
    # is_periodical() не переопределяем — наследуется (False)

    def get_info(self) -> str:
        base = super().get_info()
        return base + f"\n  Предмет: {self.subject}"
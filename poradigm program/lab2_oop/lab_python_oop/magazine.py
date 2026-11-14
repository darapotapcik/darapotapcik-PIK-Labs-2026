from .printed_edition import PrintedEdition


class Magazine(PrintedEdition):
    """Журнал: периодическое издание."""

    def __init__(self, title: str, pages: int, price: float, issue_number: int):
        super().__init__(title, pages, price)
        self.issue_number = issue_number

    @property
    def issue_number(self) -> int:
        """Номер выпуска."""
        return self.__issue_number

    @issue_number.setter
    def issue_number(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Номер выпуска должен быть положительным целым числом")
        self.__issue_number = value

    def get_category(self) -> str:
        return "Журнал"

    def illustrations_percent(self) -> int:
        return 10

    def is_periodical(self) -> bool:
        # Переопределяем метод родителя: журнал периодический
        return True

    def get_info(self) -> str:
        # Перегрузка метода родителя: добавляем номер выпуска
        base = super().get_info()
        return base + f"\n  Номер выпуска: {self.issue_number}"
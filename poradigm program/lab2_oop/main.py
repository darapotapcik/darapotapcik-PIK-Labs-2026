from colorama import init, Fore, Style
from lab_python_oop.magazine import Magazine
from lab_python_oop.book import Book
from lab_python_oop.textbook import Textbook
init(autoreset=True)
def print_title(text):
    """Заголовок раздела (голубой, жирный)."""
    print(Fore.CYAN + Style.BRIGHT + f"\n=== {text} ===" + Style.RESET_ALL)
    print(Fore.CYAN + "-" * 60 + Style.RESET_ALL)
def print_success(text):
    """Сообщение об успехе (зелёное)."""
    print(Fore.GREEN + text + Style.RESET_ALL)
def print_error(text):
    """Сообщение об ошибке (красное, жирное)."""
    print(Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)
def print_menu_item(key, text):
    """Пункт меню (жёлтый ключ, обычный текст)."""
    print(Fore.YELLOW + Style.BRIGHT + f"  {key}" + Style.RESET_ALL + f" — {text}")
def color_for(edition):
    """Цвет для типа издания."""
    if isinstance(edition, Magazine):
        return Fore.MAGENTA
    if isinstance(edition, Book):
        return Fore.GREEN
    if isinstance(edition, Textbook):
        return Fore.YELLOW
    return Fore.WHITE
def print_edition(edition, index=None):
    """Вывод издания с цветом по типу."""
    color = color_for(edition)
    prefix = f"[{index}] " if index is not None else ""
    print(color + Style.BRIGHT + prefix + edition.__class__.__name__ + Style.RESET_ALL)
    print(color + str(edition) + Style.RESET_ALL)
    print(Fore.CYAN + "-" * 60 + Style.RESET_ALL)
def demo_editions():
    """Демонстрационный набор изданий."""
    return [
        Magazine("Наука и жизнь", 100, 250.0, issue_number=12),
        Book("Война и мир", 1300, 1500.0, author="Л. Н. Толстой"),
        Textbook("Алгебра 9 класс", 300, 700.0, subject="Математика"),
    ]
def create_by_choice(choice):
    """Создаёт издание по выбору пользователя."""
    try:
        if choice == "1":
            title = input("Название журнала: ")
            pages = int(input("Страниц: "))
            price = float(input("Цена: "))
            issue = int(input("Номер выпуска: "))
            return Magazine(title, pages, price, issue)
        elif choice == "2":
            title = input("Название книги: ")
            pages = int(input("Страниц: "))
            price = float(input("Цена: "))
            author = input("Автор: ")
            return Book(title, pages, price, author)
        elif choice == "3":
            title = input("Название учебника: ")
            pages = int(input("Страниц: "))
            price = float(input("Цена: "))
            subject = input("Предмет: ")
            return Textbook(title, pages, price, subject)
        return None
    except ValueError as e:
        print_error(f"Ошибка ввода: {e}")
        return None

def main():
    print_title("Демонстрация иерархии классов 'Печатное издание'")
    print_success("Демонстрационные объекты:")
    for i, ed in enumerate(demo_editions(), start=1):
        print_edition(ed, index=i)
    while True:
        print_title("Меню")
        print_menu_item("1", "Создать журнал")
        print_menu_item("2", "Создать книгу")
        print_menu_item("3", "Создать учебник")
        print_menu_item("4", "Показать всех (демо)")
        print_menu_item("0", "Выход")
        choice = input("Ваш выбор: ").strip()
        if choice == "0":
            print_success("До свидания!")
            break
        elif choice == "4":
            print_success("Все объекты:")
            for i, ed in enumerate(demo_editions(), start=1):
                print_edition(ed, index=i)
        elif choice in ("1", "2", "3"):
            ed = create_by_choice(choice)
            if ed is not None:
                print()
                print_edition(ed)
        else:
            print_error("Неверный ввод. Попробуйте снова.")

    # Демонстрация внешнего пакета colorama
    print_title("Демонстрация внешнего пакета colorama")
    print_success("Этот текст зелёный — colorama работает.")
    print_error("А этот текст красный.")

if __name__ == "__main__":
    main()
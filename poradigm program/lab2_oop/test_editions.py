import unittest
from lab_python_oop.magazine import Magazine
from lab_python_oop.book import Book
from lab_python_oop.textbook import Textbook


class TestEditions(unittest.TestCase):

    def test_magazine_category(self):
        m = Magazine("Наука", 100, 250.0, 12)
        self.assertEqual(m.get_category(), "Журнал")

    def test_book_category(self):
        b = Book("Война и мир", 1300, 1500.0, "Толстой")
        self.assertEqual(b.get_category(), "Книга")

    def test_textbook_category(self):
        t = Textbook("Алгебра", 300, 700.0, "Математика")
        self.assertEqual(t.get_category(), "Учебник")

    def test_magazine_is_periodical(self):
        m = Magazine("Наука", 100, 250.0, 12)
        self.assertTrue(m.is_periodical())

    def test_book_not_periodical(self):
        b = Book("Война и мир", 1300, 1500.0, "Толстой")
        self.assertFalse(b.is_periodical())

    def test_textbook_not_periodical(self):
        t = Textbook("Алгебра", 300, 700.0, "Математика")
        self.assertFalse(t.is_periodical())

    def test_magazine_characters(self):
        m = Magazine("Наука", 100, 250.0, 12)
        self.assertEqual(m.characters_count(), 162000)

    def test_book_characters(self):
        b = Book("Война и мир", 1000, 1500.0, "Толстой")
        self.assertEqual(b.characters_count(), 1530000)

    def test_textbook_characters(self):
        t = Textbook("Алгебра", 100, 700.0, "Математика")
        self.assertEqual(t.characters_count(), 135000)

    def test_invalid_pages(self):
        with self.assertRaises(ValueError):
            Magazine("Наука", 0, 250.0, 12)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Book("Книга", 100, -5.0, "Автор")

    def test_cannot_instantiate_base(self):
        from lab_python_oop.printed_edition import PrintedEdition
        with self.assertRaises(TypeError):
            PrintedEdition("X", 10, 100.0)


if __name__ == "__main__":
    unittest.main()
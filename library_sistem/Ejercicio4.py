from enum import Enum


class BookGenre(Enum):
    FICTION = "Ficción"
    NONFICTION = "No Ficción"
    SCIENCE = "Ciencia"
    ART = "Arte"


class Book:
    def __init__(self, title: str, author: str, genre: BookGenre):
        """Constructor que inicializa título, autor, género y estado."""
        self._title = title
        self._author = author
        self._genre = genre
        self._is_borrowed = False

    def get_title(self) -> str:
        """Retorna el título del libro."""
        return self._title

    def get_author(self) -> str:
        """Retorna el autor del libro."""
        return self._author

    def get_genre(self) -> BookGenre:
        """Retorna el género del libro."""
        return self._genre

    def is_available(self) -> bool:
        """Retorna True si el libro está disponible, False si está prestado."""
        return not self._is_borrowed

    def set_title(self, title: str) -> None:
        """Establece el título del libro."""
        self._title = title

    def set_author(self, author: str) -> None:
        """Establece el autor del libro."""
        self._author = author

    def set_genre(self, genre: BookGenre) -> None:
        """Establece el género del libro."""
        self._genre = genre

    def set_borrowed(self, borrowed: bool) -> None:
        """Establece el estado de préstamo del libro."""
        self._is_borrowed = borrowed
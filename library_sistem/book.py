from enum import Enum


class BookGenre(Enum):
    FICTION = "Ficción"
    NONFICTION = "No Ficción"
    SCIENCE = "Ciencia"
    ART = "Arte"


class Book:
    def __init__(self, title: str, author: str, genre: BookGenre):
        self._title = title
        self._author = author
        self._genre = genre
        self._is_borrowed = False

    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

    def get_genre(self) -> BookGenre:
        return self._genre

    def is_available(self) -> bool:
        return not self._is_borrowed

    def set_title(self, title: str) -> None:
        self._title = title

    def set_author(self, author: str) -> None:
        self._author = author

    def set_genre(self, genre: BookGenre) -> None:
        self._genre = genre

    def set_borrowed(self, borrowed: bool) -> None:
        self._is_borrowed = borrowed

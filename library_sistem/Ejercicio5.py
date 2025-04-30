from typing import List
from library_sistem.Ejercicio4 import Book, BookGenre



class User:
    def __init__(self, user_id: str, name: str):
        """Constructor que inicializa ID, nombre y historial de préstamos."""
        self._user_id = user_id
        self._name = name
        self._loan_history: List[Book] = []

    def get_user_id(self) -> str:
        """Retorna el ID del usuario."""
        return self._user_id

    def get_name(self) -> str:
        """Retorna el nombre del usuario."""
        return self._name

    def get_loan_history(self) -> List[Book]:
        """Retorna el historial de préstamos."""
        return self._loan_history

    def borrow_book(self, book: Book) -> bool:
        """Toma prestado un libro si está disponible y lo agrega al historial."""
        if book.is_available():
            book.set_borrowed(True)
            self._loan_history.append(book)
            return True
        return False

    def return_book(self, book: Book) -> bool:
        """Devuelve un libro si está en el historial y actualiza su estado."""
        if book in self._loan_history:  
            book.set_borrowed(False)
            return True
        return False


class Employee:
    def __init__(self, employee_id: str, name: str):
        """Constructor que inicializa ID y nombre del empleado."""
        self._employee_id = employee_id
        self._name = name

    def get_employee_id(self) -> str:
        """Retorna el ID del empleado."""
        return self._employee_id

    def get_name(self) -> str:
        """Retorna el nombre del empleado."""
        return self._name

    def add_user(self, user: User, user_list: List[User]) -> None:
        """Agrega un usuario a la lista de usuarios."""
        if user not in user_list:
            user_list.append(user)

    def remove_user(self, user: User, user_list: List[User]) -> bool:
        """Elimina un usuario de la lista si existe."""
        if user in user_list:
            user_list.remove(user)
            return True
        return False

    def update_book_info(self, book: Book, title: str = None, author: str = None, genre: BookGenre = None) -> None:
        """Actualiza la información de un libro (título, autor o género)."""
        if title:
            book.set_title(title)
        if author:
            book.set_author(author)
        if genre:
            book.set_genre(genre)
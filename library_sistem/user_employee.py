from typing import List
from book import Book, BookGenre


class User:
    def __init__(self, user_id: str, name: str):
        self._user_id = user_id
        self._name = name
        self._loan_history: List[Book] = []

    def get_user_id(self) -> str:
        return self._user_id

    def get_name(self) -> str:
        return self._name

    def get_loan_history(self) -> List[Book]:
        return self._loan_history

    def borrow_book(self, book: Book) -> bool:
        if book.is_available():
            book.set_borrowed(True)
            self._loan_history.append(book)
            return True
        return False

    def return_book(self, book: Book) -> bool:
        if book in self._loan_history:
            book.set_borrowed(False)
            return True
        return False


class Employee:
    def __init__(self, employee_id: str, name: str):
        self._employee_id = employee_id
        self._name = name

    def get_employee_id(self) -> str:
        return self._employee_id

    def get_name(self) -> str:
        return self._name

    def add_user(self, user: User, user_list: List[User]) -> None:
        if user not in user_list:
            user_list.append(user)

    def remove_user(self, user: User, user_list: List[User]) -> bool:
        if user in user_list:
            user_list.remove(user)
            return True
        return False

    def update_book_info(self, book: Book, title: str = None, author: str = None, genre: BookGenre = None) -> None:
        if title:
            book.set_title(title)
        if author:
            book.set_author(author)
        if genre:
            book.set_genre(genre)

from typing import List
import json
import gradio as gr
from book import Book, BookGenre
from user_employee import User, Employee


class Library:
    def __init__(self):
        self._books: List[Book] = []
        self._users: List[User] = []
        self._employee = Employee("E001", "Admin")
        self.add_book("Cien años de soledad", "Gabriel García Márquez", "FICTION")
        self.add_book("Sapiens", "Yuval Noah Harari", "NONFICTION")
        self.add_user("U001", "Ana López")

    def add_book(self, title: str, author: str, genre: str) -> str:
        try:
            genre_enum = BookGenre[genre.upper()]
            book = Book(title, author, genre_enum)
            self._books.append(book)
            return f"Libro '{title}' agregado exitosamente."
        except KeyError:
            return f"Error: Género '{genre}' no válido. Use: FICTION, NONFICTION, SCIENCE, ART."

    def add_user(self, user_id: str, name: str) -> str:
        user = User(user_id, name)
        self._employee.add_user(user, self._users)
        return f"Usuario '{name}' agregado exitosamente."

    def find_book_by_title(self, title: str) -> Book:
        for book in self._books:
            if book.get_title().lower() == title.lower():
                return book  
        return None

    def find_user_by_id(self, user_id: str) -> User:
        for user in self._users:
            if user.get_user_id() == user_id:
                return user
        return None

    def borrow_book(self, user_id: str, book_title: str) -> str:
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_title(book_title)
        if user and book:
            if user.borrow_book(book):
                return f"{user.get_name()} tomó prestado '{book.get_title()}'."
            else:
                return f"El libro '{book.get_title()}' no está disponible."
        else:
            return "Usuario o libro no encontrado."

    def return_book(self, user_id: str, book_title: str) -> str:
        user = self.find_user_by_id(user_id)
        book = self.find_book_by_title(book_title)
        if user and book:
            if user.return_book(book):
                return f"{user.get_name()} devolvió '{book.get_title()}'."
            else:
                return f"El libro '{book.get_title()}' no está en el historial de {user.get_name()}."
        else:
            return "Usuario o libro no encontrado."

    def check_availability(self, book_title: str) -> str:
        book = self.find_book_by_title(book_title)
        if book:
            status = "disponible" if book.is_available() else "prestado"
            return f"El libro '{book.get_title()}' está {status}."
        else:
            return f"El libro '{book_title}' no está en la biblioteca."

    def list_books(self) -> List[List[str]]:
        return [[book.get_title(), book.get_author(), book.get_genre().name, "Disponible" if book.is_available() else "Prestado"] for book in self._books]

    def list_users(self) -> List[List[str]]:
        return [[user.get_user_id(), user.get_name(), ", ".join([b.get_title() for b in user.get_loan_history()])] for user in self._users]

    def save_state(self) -> str:
        state = {
            "books": [
                {
                    "title": book.get_title(),
                    "author": book.get_author(),
                    "genre": book.get_genre().name,
                    "is_borrowed": not book.is_available()
                } for book in self._books
            ],
            "users": [
                {
                    "user_id": user.get_user_id(),
                    "name": user.get_name(),
                    "loan_history": [b.get_title() for b in user.get_loan_history()]
                } for user in self._users
            ]
        }
        try:
            with open("library_state.json", 'w') as f:
                json.dump(state, f, indent=2)
            return "Estado guardado en 'library_state.json'."
        except IOError:
            return "Error al guardar el estado."


def create_gradio_interface():
    library = Library()
    with gr.Blocks(title="Sistema de Gestión de Biblioteca") as demo:
        gr.Markdown("# Sistema de Gestión de Biblioteca")
        

        with gr.Tab("Agregar Libro"):
            book_title = gr.Textbox(label="Título del libro")
            book_author = gr.Textbox(label="Autor del libro")
            book_genre = gr.Dropdown(choices=["FICTION", "NONFICTION", "SCIENCE", "ART"], label="Género")
            add_book_btn = gr.Button("Agregar Libro")
            book_output = gr.Textbox(label="Resultado")
            add_book_btn.click(
                fn=library.add_book,
                inputs=[book_title, book_author, book_genre],
                outputs=book_output
            )


        with gr.Tab("Agregar Usuario"):
            user_id = gr.Textbox(label="ID del usuario")
            user_name = gr.Textbox(label="Nombre del usuario")
            add_user_btn = gr.Button("Agregar Usuario")
            user_output = gr.Textbox(label="Resultado")
            add_user_btn.click(
                fn=library.add_user,
                inputs=[user_id, user_name],
                outputs=user_output
            )


        with gr.Tab("Prestar Libro"):
            borrow_user_id = gr.Textbox(label="ID del usuario")
            borrow_book_title = gr.Textbox(label="Título del libro")
            borrow_btn = gr.Button("Prestar Libro")
            borrow_output = gr.Textbox(label="Resultado")
            borrow_btn.click(
                fn=library.borrow_book,
                inputs=[borrow_user_id, borrow_book_title],
                outputs=borrow_output
            )


        with gr.Tab("Devolver Libro"):
            return_user_id = gr.Textbox(label="ID del usuario")
            return_book_title = gr.Textbox(label="Título del libro")
            return_btn = gr.Button("Devolver Libro")
            return_output = gr.Textbox(label="Resultado")
            return_btn.click(
                fn=library.return_book,
                inputs=[return_user_id, return_book_title],
                outputs=return_output
            )


        with gr.Tab("Consultar Disponibilidad"):
            check_book_title = gr.Textbox(label="Título del libro")
            check_btn = gr.Button("Consultar")
            check_output = gr.Textbox(label="Resultado")
            check_btn.click(
                fn=library.check_availability,
                inputs=check_book_title,
                outputs=check_output
            )


        with gr.Tab("Listar"):
            with gr.Row():
                list_books_btn = gr.Button("Listar Libros")
                list_users_btn = gr.Button("Listar Usuarios")
            books_df = gr.Dataframe(headers=["Título", "Autor", "Género", "Estado"], label="Libros")
            users_df = gr.Dataframe(headers=["ID", "Nombre", "Historial"], label="Usuarios")
            list_books_btn.click(fn=library.list_books, outputs=books_df)
            list_users_btn.click(fn=library.list_users, outputs=users_df)


        with gr.Tab("Guardar"):
            save_btn = gr.Button("Guardar Estado")
            save_output = gr.Textbox(label="Resultado")
            save_btn.click(fn=library.save_state, outputs=save_output)

    return demo


if __name__ == "__main__":
    demo = create_gradio_interface()
    demo.launch()
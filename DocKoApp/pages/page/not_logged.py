import flet as ft
from DocKoApp.pages.components.doctor_cards import build_doctor_cards
from DocKoApp.pages.components.headers import headerPage
from DocKoApp.pages.components.login import Login
from DocKoApp.pages.components.signup import SignUp

def NotLoggedPage(page):
    lg = Login(page)
    sg = SignUp(page)
    cards = build_doctor_cards(page)

    return ft.View(
        route="/",
        controls=[
            ft.Row([
                ft.Row(
                    [headerPage()],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Spread out items
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Center items vertically
                ),
                # Signup and Login Buttons
                ft.Row([
                    ft.Container(
                        content=ft.ElevatedButton("Login", bgcolor="white", color="blue", width=150, height=50, on_click=lambda e: page.open(lg)),
                        padding=10,
                    ),
                    ft.Container(
                        content=ft.ElevatedButton("Sign Up", bgcolor="blue", color="white", width=150,height=50, on_click=lambda e: page.open(sg)),
                        padding=10,
                    ),
                    ],
                    spacing=10,
                    scroll="adaptive",
                ),
            ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Spread out items
                vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Center items vertically
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.TextField(hint_text="Search...", border_color="blue", expand=True),
                                ft.ElevatedButton("Location", icon=ft.icons.LOCATION_ON, color="blue"),
                                ft.ElevatedButton("Filter", icon=ft.icons.FILTER_ALT, color="blue"),
                            ],
                            spacing=10,
                        ),
                        ft.Text("We've found 405 Doctors/Providers you can book with!", size=14),
                    ],
                    spacing=10,
                    scroll="adaptive",
                ),
                padding=15,
                border_radius=8,
            ),
            cards,
        ],
        scroll="adaptive",
    )

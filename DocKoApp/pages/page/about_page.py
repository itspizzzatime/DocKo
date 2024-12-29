import flet as ft
from DocKoApp.pages.components.headers import headerPage
from DocKoApp.pages.components.navbar import create_navbar

def AboutPage(page):
    navbar = create_navbar(page)

    return ft.View(
        route="/about",
        navigation_bar=navbar,
        controls=[
            ft.Row(
                [headerPage()],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Spread out items
                vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Center items vertically
            ),

        ],
    )

import flet as ft
from DocKoApp.pages.components.headers import headerPage
from DocKoApp.pages.components.navbar import create_navbar

def DocumentPage(page):
    navbar = create_navbar(page)
    # Navigation between steps
    current_step = {"value": 1}
    return ft.View(
        route="/documents",
        navigation_bar=navbar,
        controls=[
            ft.Row(
                [headerPage()],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Spread out items
                vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Center items vertically
            ),

        ],
    )

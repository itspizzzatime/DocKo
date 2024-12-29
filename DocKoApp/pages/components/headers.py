# header.py
import flet as ft

def headerPage():
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Image(
                    src="assets/logo.png",
                    width=100,
                    height=100,
                ),
                ft.Text(
                    "DocKo",
                    size=40,
                    color=ft.colors.BLUE,
                    weight=ft.FontWeight.BOLD,
                ),
            ],
            alignment="center",
            spacing=10,
        ),
        margin=10,
    )

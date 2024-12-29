import flet as ft
from DocKoApp.pages.components.headers import headerPage
from DocKoApp.pages.components.navbar import create_navbar

specialties = [
        ("Dermatology", r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\icons\Dermatology.png"),
        ("Family Medicine", r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\icons\Family Medicine.png"),
        ("General Dentistry", r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\icons\General Dentistry.png"),
        ("Infectious Diseases", r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\icons\Infectious Diseases.png"),
        ("Internal Medicine", r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\icons\Internal Medicine.png"),
    ]



def ServicePage(page):
    navbar = create_navbar(page)

    cards = []

    for name, icon in specialties:
        cards.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Image(icon, width=70, height=70),
                            ft.Text(name, size=16, weight=500, text_align="center"),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=15,
                    alignment=ft.alignment.center,
                ),
                width=180,
                height=180,
            )
        )

    return ft.View(
        route="/service",
        navigation_bar=navbar,
        controls=[
            ft.Row([
                ft.Row(
                    [headerPage()],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Spread out items
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Center items vertically
                ),
            ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Spread out items
                vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Center items vertically
            ),
            ft.Row(
                controls=[
                    ft.TextField(hint_text="Search for Specialty, Hospital name, or your Doctor's name...",
                                 expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH),
                    ft.IconButton(icon=ft.icons.LOCATION_ON, tooltip="Select Location"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                controls=cards,
                spacing=15,
                run_spacing=15,
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True,
            ),
        ],
        spacing=10,
        scroll="adaptive",
    )



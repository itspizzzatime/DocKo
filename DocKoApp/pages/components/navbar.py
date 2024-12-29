import flet as ft

def create_navbar(page):
    def set_page(e):
        ind = e.control.selected_index
        if ind == 0:
            page.go("/home")
        elif ind == 1:
            page.go("/service")
        elif ind == 2:
            page.go("/booking")
        elif ind == 3:
            page.go("/profile")


    navbar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.ADD_HOME_OUTLINED,
                selected_icon=ft.icons.ADD_HOME,
                label="Home"),
            ft.NavigationBarDestination(
                icon=ft.icons.DOCUMENT_SCANNER_OUTLINED,
                selected_icon=ft.icons.DOCUMENT_SCANNER_OUTLINED,
                label="Services"),
            ft.NavigationBarDestination(
                icon=ft.icons.NOTIFICATIONS_ON_OUTLINED,
                selected_icon=ft.icons.NOTIFICATIONS_ON,
                label="Notifications"),
            ft.NavigationBarDestination(
                icon=ft.icons.PERSON_2_ROUNDED,
                selected_icon=ft.icons.PERSON_2_ROUNDED,
                label="Profile"),
        ],
        on_change=lambda e: set_page(e),
    )
    return navbar

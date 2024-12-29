import flet as ft

def create_navbar(page):
    def set_page(e):
        ind = e.control.selected_index
        if ind == 0:
            page.go("/home")
        if ind == 1:
            page.go("/dashboard")
        elif ind == 2:
            page.go("/notifications")
        elif ind == 3:
            page.go("/profile")

    navbar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.icons.ADD_HOME_OUTLINED,
                selected_icon=ft.icons.ADD_HOME,
                label="Dashboard"),
            ft.NavigationBarDestination(
                icon=ft.icons.LOCAL_GROCERY_STORE_OUTLINED,
                selected_icon=ft.icons.LOCAL_GROCERY_STORE,
                label="Notifications"),
            ft.NavigationBarDestination(
                icon=ft.icons.BEACH_ACCESS_OUTLINED,
                selected_icon=ft.icons.NOTIFICATIONS_ON,
                label="Profile")
        ],
        on_change=lambda e: set_page(e),
    )
    return navbar

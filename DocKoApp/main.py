import flet as ft
import os
import json
from DocKoApp.pages.page.not_logged import NotLoggedPage
from DocKoApp.pages.page.home_page import HomePage
from DocKoApp.pages.page.about_page import AboutPage
from DocKoApp.pages.page.services_page import ServicePage
from DocKoApp.pages.page.documents_page import DocumentPage
from DocKoApp.pages.page.profile_page import ProfilePage
from DocKoApp.pages.page.booking_page import BookingPage
from DocKoApp.pages.page.settings_page import SettingsPage
from DocKoApp.pages.page.doctor_sign_in import DocSign
from DocKoApp.doctor_specific_page.dashboard import DashboardPage
from DocKoApp.pages.page.client_booking import ClientSign

# Path to the JSON file where user data will be stored
DATA_FILE = "client.json"

# Function to load data from the JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []
def save_data(data):
    try:
        json_string = json.dumps(data)
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

users = {
    "first_name": "John",
    "middle_name": "Michael",
    "last_name": "Doe",
    "age": 28,
    "gender": "Male",
    "email": "john.doe@example.com",
    "phone": "+1234567890",
    "address": "123 Main Street, Springfield, IL, USA",
    "profile_picture": "https://www.example.com/profile_pictures/john_doe.jpg"
}


def main(page: ft.Page):
    page.title = "DocKo"
    page.scroll = "adaptive"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 20
    page.window_resizable = False
    page.favicon = r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\favicon.ico"

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(NotLoggedPage(page))
        elif page.route == "/home":
            page.views.append(DashboardPage(page))
        elif page.route == "/dashboard":
            page.views.append(DashboardPage(page))
        elif page.route == "/about":
            page.views.append(AboutPage(page))
        elif page.route == "/book":
            page.views.append(ClientSign(page))
        elif page.route == "/service":
            page.views.append(ServicePage(page))
        elif page.route == "/documents":
            page.views.append(DocumentPage(page))
        elif page.route == "/profile":
                page.views.append(ProfilePage(page, users))
        elif page.route == "/booking":
            page.views.append(BookingPage(page))
        elif page.route == "/setting":
            page.views.append(SettingsPage(page))
        elif page.route == "/docform":
            page.views.append(DocSign(page))
        else:
            page.views.append(HomePage(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)



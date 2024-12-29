import json
import flet as ft
import os

from DocKoApp.doctor_specific_page.dashboard import DashboardPage
from DocKoApp.pages.page.home_page import HomePage
from DocKoApp.db.append import append_user_to_client


# Path to the JSON file where user data is stored
DATA_FILE = "client.json"
USER_LOG = "user_log.json"

# Function to load data from the JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def Login(page: ft.Page):
    # Define the login form fields
    email = ft.TextField(label="Email", autofocus=True)
    password = ft.TextField(label="Password", password=True)
    login_message = ft.Text(value="", color="red")

    # Error message for each field
    error_email = ft.Text(value="", color="red", size=10)
    error_password = ft.Text(value="", color="red", size=10)

    def handle_login(e):
        # Reset error messages
        error_email.value = ""
        error_password.value = ""
        login_message.value = ""
        page.update()

        # Get entered credentials
        entered_email = email.value
        entered_password = password.value

        # Validation checks
        valid = True

        if not entered_email:
            error_email.value = "Email is required."
            valid = False
        if not entered_password:
            error_password.value = "Password is required."
            valid = False

        if valid:
            # Load user data from file
            users = load_data()
            # Search for a user with the matching email and password
            user = next((u for u in users if u["email"] == entered_email and u["password"] == entered_password), None)

            if user:
                # Successful login
                login_message.value = "Login successful!"
                login_message.color = ft.colors.GREEN
                append_user_to_client(DATA_FILE, USER_LOG)
                page.update()
                page.views.append(DashboardPage(page))

                # You can proceed to the next page or redirect the user here
            else:
                # Invalid credentials
                login_message.value = "Invalid email or password."
                login_message.color = ft.colors.RED
                page.update()



    # Define the login dialog
    dlg_login = ft.AlertDialog(
        modal=False,
        title=ft.Row([ft.Text("Login", color=ft.colors.BLUE, weight=ft.FontWeight.BOLD,)], alignment=ft.MainAxisAlignment.CENTER),
        content=ft.Column(
            [
                email,
                error_email,
                password,
                error_password,
                login_message,
            ],
            width=page.window.width / 3,
            height=175
        ),
        inset_padding=50,
        actions=[
            ft.Row([
                ft.ElevatedButton("Login", on_click=handle_login, bgcolor="blue", color="white", height=35),
            ], alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START)
        ],
        actions_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    return dlg_login

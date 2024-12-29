import flet as ft
import os
from DocKoApp.pages.page.doctor_sign_in import DocSign
from DocKoApp.pages.page.home_page import HomePage
import json


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


# Define the form fields
fname = ft.TextField(label="First Name", autofocus=True,  border_color=ft.Colors.BLUE)
lname = ft.TextField(label="Last Name", autofocus=True,  border_color=ft.Colors.BLUE)
email = ft.TextField(label="Email", autofocus=True,  border_color=ft.Colors.BLUE)
number = ft.TextField(label="Phone Number", autofocus=True,  border_color=ft.Colors.BLUE)
password = ft.TextField(label="Password", password=True,  border_color=ft.Colors.BLUE)
confirm_password = ft.TextField(label="Confirm Password", password=True,  border_color=ft.Colors.BLUE)
login_message = ft.Text(value="", color="red")

# Error message labels for each field with smaller font size
error_fname = ft.Text(value="", color="red", size=10)
error_lname = ft.Text(value="", color="red", size=10)
error_email = ft.Text(value="", color="red", size=10)
error_number = ft.Text(value="", color="red", size=10)
error_password = ft.Text(value="", color="red", size=10)
error_confirm_password = ft.Text(value="", color="red", size=10)
error_role = ft.Text(value="", color="red", size=10)

def SignUp(page: ft.Page):
    # Store selected role
    selected_role = None

    def on_button_click(event, role):
        nonlocal selected_role
        selected_role = role

        # Update button styles
        is_patient.style = ft.ButtonStyle(
            color=ft.colors.BLACK,
            bgcolor=ft.colors.BLUE if role == "patient" else ft.colors.WHITE,
        )
        is_doctor.style = ft.ButtonStyle(
            color=ft.colors.BLACK,
            bgcolor=ft.colors.BLUE if role == "doctor" else ft.colors.WHITE,
        )
        page.update()

        return selected_role

    def handle_sign_up(e):
        # Reset error messages
        error_fname.value = ""
        error_lname.value = ""
        error_email.value = ""
        error_number.value = ""
        error_password.value = ""
        error_confirm_password.value = ""
        error_role.value = ""
        login_message.value = ""

        page.update()

        # Validation checks
        valid = True

        if not fname.value:
            error_fname.value = "First name is required."
            valid = False
        if not lname.value:
            error_lname.value = "Last name is required."
            valid = False
        if not email.value:
            error_email.value = "Email is required."
            valid = False
        if not number.value:
            error_number.value = "Phone number is required."
            valid = False
        if not password.value:
            error_password.value = "Password is required."
            valid = False
        if password.value != confirm_password.value:
            error_confirm_password.value = "Passwords do not match."
            valid = False
        if not selected_role:
            error_role.value = "Please select a role (Patient or Doctor)."
            valid = False

        # If the data is valid, proceed to save
        if valid:
            # Collect user data
            user_data = {
                "fname": fname.value,
                "lname": lname.value,
                "email": email.value,
                "number": number.value,
                "role": selected_role,
                "password": password.value,  # Do not store plaintext passwords in production
            }

            # Load existing data
            users = load_data()
            # Append new user
            users.append(user_data)
            # Save updated data to JSON file
            save_data(users)

            # Clear input fields and show a success message
            fname.value = ""
            lname.value = ""
            email.value = ""
            number.value = ""
            password.value = ""
            confirm_password.value = ""
            login_message.value = "Signup successful!"
            login_message.color = ft.colors.GREEN
            #if the role is doctor, go to another page
            page.views.append(DocSign(page)) if selected_role == "doctor" else page.views.append(HomePage(page))


    # Role selection buttons
    is_patient = ft.ElevatedButton(
        text="Patient",
        icon=ft.icons.PERSON,
        on_click=lambda e: on_button_click(e, "patient"),
        style=ft.ButtonStyle(
            color=ft.colors.BLACK,
            bgcolor=ft.colors.WHITE,
        ),
    )

    is_doctor = ft.ElevatedButton(
        text="Doctor",
        icon=ft.icons.MONITOR_HEART,
        on_click=lambda e: on_button_click(e, "doctor"),
        style=ft.ButtonStyle(
            color=ft.colors.BLACK,
            bgcolor=ft.colors.WHITE,
        ),
    )

    dlg_signup = ft.AlertDialog(
        modal=False,
        title=ft.Row([ft.Text("Sign Up", color=ft.colors.BLUE, weight=ft.FontWeight.BOLD,)], alignment=ft.MainAxisAlignment.CENTER),
        content=ft.Column(
            [
                ft.Row([fname, lname], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                ft.Row([error_fname, error_lname], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                ft.Row([email, number], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                ft.Row([error_email, error_number], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                password,
                error_password,
                confirm_password,
                error_confirm_password,
                ft.Row([ft.Text("I am a ")], alignment=ft.MainAxisAlignment.SPACE_AROUND),
                ft.Row([is_patient, is_doctor], alignment=ft.MainAxisAlignment.CENTER),
                error_role,
                login_message,
            ],
            width=page.window.width / 2,
        ),
        inset_padding=50,
        actions=[
            ft.ElevatedButton("Sign Up", on_click=handle_sign_up, bgcolor="blue", color="white", width=120,height=40,),
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
    )

    return dlg_signup

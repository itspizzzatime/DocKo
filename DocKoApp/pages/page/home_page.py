import flet as ft
import json
import os
from DocKoApp.pages.components.doctor_cards import build_doctor_cards
from DocKoApp.pages.components.headers import headerPage
from DocKoApp.pages.components.navbar import create_navbar

DATA_FILE = "form_data.json"

# Function to load data from the JSON file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            print("hje")
            return json.load(file)
    else:
        print("shit")
    return []

def save_data(data):
    try:
        print("Saving data:", data)  # Print data before saving
        # Try serializing the data to a string to confirm its valid JSON
        json_string = json.dumps(data)
        print("Serialized data:", json_string)  # Print the serialized data

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Error saving data: {e}")

def get_last_name(file_path):
    try:
        with open(file_path, "r") as file:
            user_log = json.load(file)
            if user_log:  # Ensure the list is not empty
                last_user = user_log[-1]
                full_name = f"{last_user.get('fname', 'Unknown')} {last_user.get('lname', 'Unknown')}"
                return full_name
            else:
                return "No users in the log."
    except Exception as e:
        return f"Error reading file: {e}"

def HomePage(page):
    navbar = create_navbar(page)
    cards = build_doctor_cards(page)

    return ft.View(
        route="/home",
        navigation_bar=navbar,
        controls=[
            ft.Row(
                [headerPage(),
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
                        ft.Text("We've found  Doctors/Providers you can book with!", size=14),
                    ],
                    spacing=10,
                    scroll="adaptive",
                ),
                padding=15,
                border_radius=8,
            ),
            cards
        ],
        scroll="adaptive",
    )



import flet as ft
import json
import os
from DocKoApp.pages.components.notifications import create_notification_card, notification_card
from DocKoApp.pages.components.headers import headerPage
from DocKoApp.doctor_specific_page.doc_navbar import create_navbar

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

def DashboardPage(page):
    navbar = create_navbar(page)

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
                        notification_card
                    ],
                    spacing=10,
                    scroll="adaptive",
                ),
                padding=15,
                border_radius=8,
            ),

        ],
        scroll="adaptive",
    )



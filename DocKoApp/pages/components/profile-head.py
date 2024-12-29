import flet as ft
import json
import os
from DocKoApp.pages.components.doctor_cards import create_doctor_card, doctors
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

def ProfileHead():
    name = load_data()
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

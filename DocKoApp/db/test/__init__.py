import flet as ft
from search import create_search_box, search_doctors
from cards import build_doctor_cards

# Sample doctors data
doctors = [
    ("Dr. Emelito Galeos", "RN, MD - Obstetrician-Gynecology - Reproductive Health", "3", False, True, "07:00 AM - 10:00 PM", "₱400.00", "University of Santo Tomas Hospital", "doctor_image_1.jpg"),
    ("Dr. Jan Jorge Francisco", "MD, FPOGS, FPSUOG Obstetrics and Gynecology OB-GYN Ultrasound", "10", True, True, "Tomorrow, 03:00 PM - 05:00 PM", "₱700.00", "Delos Santos Medical Center RM", "doctor_image_2.jpg"),
    ("Dr. Anna Celinna Velenzuela", "MD, DPPS General Pediatrics", "9", True, True, "Tomorrow, 03:00 PM - 05:00 PM", "₱700.00", "Delos Santos Medical Center RM", "doctor_image_3.jpg"),
    # Add more doctor data here...
]

# Callback function for booking appointments
def on_book_appointment(e):
    print("Booking appointment...")  # Placeholder for actual booking logic
    # You can add navigation or appointment logic here, if needed.

# Main page function
def home_page(page):
    global search_input, doctor_cards

    # Search bar input field
    search_input = create_search_box(lambda e: search_doctors(e, doctors, doctor_cards, page))

    # Container to hold doctor cards
    doctor_cards = build_doctor_cards(page, doctors, on_book_appointment)

    # Add the search box and doctor cards to the page
    page.add(search_input, doctor_cards)

# Run the app
ft.app(target=home_page)

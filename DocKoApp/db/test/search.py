import flet as ft

# Function to search doctors by name or specialty
def search_doctors(e, doctors, doctor_cards, page):
    search_term = e.control.value.lower()

    # Filter doctors by name or specialty
    filtered_doctors = [
        doctor for doctor in doctors
        if search_term in doctor[0].lower() or search_term in doctor[1].lower()
    ]

    # Update the list of doctor cards without clearing the entire page
    doctor_cards.controls.clear()

    # Add filtered doctor cards
    for doctor in filtered_doctors:
        doctor_cards.controls.append(doctor[0])

    # Update the doctor's list display only
    page.update()

# Function to create the search box
def create_search_box(on_search_change):
    return ft.TextField(
        hint_text="Search by name or specialty...",
        border_color="blue",
        expand=True,
        on_change=on_search_change
    )

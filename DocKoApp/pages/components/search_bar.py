import flet as ft


def search_doctors(e):
    search_term = search_input.value.lower()

    # Filter doctors by name or specialty
    filtered_doctors = [
        doctor for doctor in doctors
        if search_term in doctor[0].lower() or search_term in doctor[1].lower()
    ]

    # Update the list of doctor cards without clearing the entire page
    doctor_cards.controls.clear()

    for doctor in filtered_doctors:
        doctor_cards.controls.append(create_doctor_card(*doctor))

    # Update the doctor's list display only
    page.update()


# Search bar input
search_input = ft.TextField(
    hint_text="Search by name or specialty...",
    border_color="blue",
    expand=True,
    on_change=search_doctors
)

def main(page: ft.Page):
    # Initialize the buttons with initial state (not selected)
    patient_button = ft.ElevatedButton(
        text="Patient",
        icon=ft.icons.PERSON,  # Icon for Patient
        on_click=lambda e: on_button_click(e, "patient"),
        style=ft.ButtonStyle(
            color=ft.colors.BLACK,
            bgcolor=ft.colors.LIGHT_BLUE
        ),
    )

    doctor_button = ft.ElevatedButton(
        text="Doctor",
        icon=ft.icons.MONITOR_HEART,  # Icon for Doctor
        on_click=lambda e: on_button_click(e, "doctor"),
        style=ft.ButtonStyle(
            color=ft.colors.BLACK,
            bgcolor=ft.colors.LIGHT_GREEN
        ),
    )

    # Store selected button state
    selected = None

    def on_button_click(event, selected_role):
        nonlocal selected
        # Update selected button
        if selected == selected_role:
            selected = None
        else:
            selected = selected_role

        # Update the button styles based on selection state
        patient_button.style = ft.ButtonStyle(
            color=ft.colors.BLACK,
            bgcolor=ft.colors.LIGHT_BLUE if selected != "patient" else ft.colors.BLUE,
        )
        doctor_button.style = ft.ButtonStyle(
            color=ft.colors.BLACK,
            bgcolor=ft.colors.LIGHT_GREEN if selected != "doctor" else ft.colors.GREEN,
        )

        # Update the page to reflect changes
        page.update()

    def on_submit_click(event):
        # Check if patient is selected and show appropriate message
        if selected == "patient":
            page.controls.append(ft.Text("Hello"))
        else:
            page.controls.append(ft.Text("Hi"))

        # Update the page to reflect the new text
        page.update()

    # Create a Submit button
    submit_button = ft.ElevatedButton(
        text="Submit",
        on_click=on_submit_click,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.PURPLE
        ),
    )

    # Add buttons and the submit button to the page
    page.add(patient_button, doctor_button, submit_button)


ft.app(target=main)

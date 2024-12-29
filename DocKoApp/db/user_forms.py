import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "User Registration and Health Information Form"
    page.scroll = "adaptive"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 20
    page.bgcolor = ft.Colors.LIGHT_BLUE_50

    # Navigation between steps
    current_step = {"value": 1}

    # Form data storage
    form_data = {}

    def validate_inputs():
        """Validates the inputs for the current step."""
        current_controls = step_container.controls[0].controls
        checkbox_checked = False  # Flag to track if at least one checkbox is checked

        for control in current_controls:
            if isinstance(control, ft.TextField):
                if not control.value.strip() and "Optional" not in control.label:
                    error_text.value = "Please fill out all required fields."
                    return False
                if control.label.startswith("Postal Code") and (
                        not control.value.isdigit() or len(control.value) != 4):
                    error_text.value = "The postal code requires 4 digits."
                    return False
                if control.label.startswith("Phone Number") and (
                        not control.value.isdigit() or len(control.value) != 11):
                    error_text.value = "The phone number requires 11 digits."
                    return False
            if isinstance(control, ft.RadioGroup) and not control.value:
                error_text.value = "Please select an option."
                return False
            if isinstance(control, ft.Checkbox):
                if control.value:
                    checkbox_checked = True  # At least one checkbox is checked
            if isinstance(control, ft.Dropdown) and not control.value and "Optional" not in control.label:
                error_text.value = "Please select an option from the dropdown."
                return False
            if isinstance(control, ft.DatePicker) and "dob" not in form_data:
                error_text.value = "Please pick a date."
                return False

        # After checking all controls, verify if at least one checkbox is checked
        if any(isinstance(control, ft.Checkbox) for control in current_controls) and not checkbox_checked:
            error_text.value = "Please check at least one required box."
            return False

        return True

    def next_step(e):
        """Proceeds to the next step, validates inputs first."""
        if not validate_inputs():
            page.update()  # Ensure the error message is displayed
            return

        if current_step["value"] < 7:  # Move to the next step if within bounds
            current_step["value"] += 1
            update_form()

    def previous_step(e):
        """Goes back to the previous step."""
        if current_step["value"] > 1:
            current_step["value"] -= 1
            update_form()

    def update_form():
        """Updates the form display based on the current step."""
        error_text.value = ""
        progress_bar.value = current_step["value"] / 7
        step_container.controls.clear()
        step_container.controls.append(build_form_step(current_step["value"]))
        page.update()

    def build_form_step(step):
        if step == 1:
            # Displays and Updates DOB based on the date picked.
            dob_display = ft.Container(
                ft.Text("Date of Birth: Not selected", size=16, color=ft.Colors.BLACK),
                border=ft.border.all(1, ft.Colors.BLUE),
                padding=6,
                margin=ft.margin.only(top=5, bottom=5),
                width=250,
            )

            def update_dob(e):
                # Save the selected date to form_data
                form_data["dob"] = e.control.value
                dob_display.content = ft.Text(f"Date of Birth: {form_data['dob'].strftime('%Y-%m-%d')}", color=ft.Colors.BLACK)  # Update display
                page.update()

            return ft.Column(
                [
                    ft.Text("Step 1: Account Setup", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                    ft.TextField(label="First Name", border_color=ft.Colors.BLUE, color=ft.Colors.BLACK),
                    ft.TextField(label="Middle Name (Optional)", border_color=ft.Colors.BLUE, color=ft.Colors.BLACK),
                    ft.TextField(label="Last Name", border_color=ft.Colors.BLUE, color=ft.Colors.BLACK),
                    ft.ElevatedButton(
                        "Pick Date of Birth",
                        icon=ft.Icons.CALENDAR_MONTH,
                        on_click=lambda _: page.open(
                            ft.DatePicker(
                                first_date=datetime.datetime(year=1900, month=1, day=1),
                                last_date=datetime.datetime(year=2024, month=12, day=31),
                                help_text="Select your date of birth",
                                barrier_color=ft.Colors.WHITE,
                                on_change=update_dob,
                            )
                        ),
                    ),
                    dob_display,
                    ft.Dropdown(
                        label="Gender",
                        options=[
                            ft.dropdown.Option("Male"),
                            ft.dropdown.Option("Female"),
                            ft.dropdown.Option("Non-Binary"),
                            ft.dropdown.Option("Prefer not to say"),
                            ft.dropdown.Option("Other"),
                        ],
                        border_color=ft.Colors.BLUE,
                        bgcolor=ft.Colors.WHITE,
                        color=ft.Colors.BLACK,
                    ),
                ]
            )

        elif step == 2:
            return ft.Column(
                [
                    ft.Text("Step 2: Contact Information", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),

                    # Country dropdown
                    ft.Dropdown(
                        label="Country",
                        options=[ft.dropdown.Option("Philippines")],
                        border_color=ft.Colors.BLUE,
                        bgcolor=ft.Colors.WHITE,
                        color=ft.Colors.BLACK
                    ),

                    # State/Province dropdown
                    ft.Dropdown(
                        label="State/Province",
                        options=[
                            ft.dropdown.Option("Metro Manila"),
                            ft.dropdown.Option("Central Visayas"),
                            ft.dropdown.Option("Davao Region"),
                            ft.dropdown.Option("Cordillera Administrative Region"),
                        ],
                        border_color=ft.Colors.BLUE,
                        bgcolor=ft.Colors.WHITE,
                        color=ft.Colors.BLACK
                    ),

                    # City dropdown
                    ft.Dropdown(
                        label="City",
                        options=[
                            ft.dropdown.Option("Manila"),
                            ft.dropdown.Option("Quezon City"),
                            ft.dropdown.Option("Cebu City"),
                            ft.dropdown.Option("Davao City"),
                            ft.dropdown.Option("Baguio"),
                        ],
                        border_color=ft.Colors.BLUE,
                        bgcolor=ft.Colors.WHITE,
                        color=ft.Colors.BLACK
                    ),

                    # Street Address input
                    ft.TextField(
                        label="Street Address",
                        border_color=ft.Colors.BLUE,
                        color=ft.Colors.BLACK
                    ),

                    # Postal Code input
                    ft.TextField(
                        label="Postal Code",
                        border_color=ft.Colors.BLUE,
                        keyboard_type=ft.KeyboardType.NUMBER,
                        max_length=4,  # Limit the postal code to 4 digits
                        color=ft.Colors.BLACK
                    ),

                    # Phone Number input with validation for 11 digits
                    ft.TextField(
                        label="Phone Number",
                        border_color=ft.Colors.BLUE,
                        keyboard_type=ft.KeyboardType.NUMBER,
                        color=ft.Colors.BLACK,
                        max_length=11,

                    )
                ]
            )

        elif step == 3:
            return ft.Column(
                [
                    ft.Text("Step 3: Health Information", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                    ft.Text("Symptoms or Health Concerns", size=16, color=ft.Colors.BLUE),
                    ft.Divider(color=ft.Colors.BLUE),
                    ft.Checkbox(label="General Symptoms"),
                    ft.Checkbox(label="Pain or Discomfort"),
                    ft.Checkbox(label="Digestive Issues"),
                    ft.Checkbox(label="Skin or Dermatological Symptoms"),
                    ft.Checkbox(label="Mental Health Symptoms"),
                    ft.TextField(
                        label="Other Symptoms (Optional)",
                        border_color=ft.Colors.BLUE,
                        bgcolor=ft.Colors.WHITE,
                        color=ft.Colors.BLACK,
                        max_lines=10,  # Maximum number of lines before scrolling
                        height=100,  # Height of the text field
                        multiline=True,  # Enables multi-line input
                    )
                ]
            )

        elif step == 4:
            return ft.Column(
                [
                    ft.Text("Step 4: Doctor or Hospital Preferences", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                    ft.Checkbox(label="General Practitioner (GP)", check_color=ft.Colors.BLUE),
                    ft.Checkbox(label="Dentist", check_color=ft.Colors.BLUE),
                    ft.Checkbox(label="Psychiatrist", check_color=ft.Colors.BLUE),
                    ft.Checkbox(label="Dermatologist", check_color=ft.Colors.BLUE),
                    ft.Checkbox(label="Obstetrician/Gynecologist", check_color=ft.Colors.BLUE),
                    ft.TextField(label="Specialist (Optional)", border_color=ft.Colors.BLUE,color=ft.Colors.BLACK),

                ]
            )
        elif step == 5:
            distance_text = ft.Text("Selected distance: 5 km", size=16, color=ft.Colors.BLACK)

            def update_distance(e):
                # Update the text to show the new distance
                distance_text.value = f"Selected distance: {int(e.control.value)} km"
                # Ensure the page is updated to reflect the change in the text element
                e.control.page.update()

            return ft.Column(
                [
                    ft.Text("Step 5: Location and Proximity", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                    ft.Text("Preferred distance radius for searching", size=16, color=ft.Colors.BLUE),
                    distance_text,  # Display the selected distance
                    ft.Slider(
                        min=1,  # Minimum value of 1 km
                        max=200,  # Maximum value of 200 km
                        divisions=200,  # Number of discrete steps
                        value=5,  # Default value
                        on_change=update_distance,  # Handle the slider value change
                        active_color=ft.Colors.BLUE,
                        thumb_color=ft.Colors.BLUE,
                        label="{value} km",
                        inactive_color='#808080',  # Inactive slider color
                    ),
                ],
                spacing=10  # Space between the elements
            )

        elif step == 6:
            return ft.Column(
                [
                    ft.Text("Step 6: Privacy and Consent", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                    ft.Checkbox(label="I agree to the terms and conditions", check_color=ft.Colors.BLUE),
                    ft.Checkbox(label="I consent to the collection and use of my health data",
                                check_color=ft.Colors.BLUE),
                    ft.Text(
                        "Welcome to DocKo, your trusted healthcare appointment booking app. Please read these Terms and Conditions carefully before using our services. By registering for and using DocKo, you agree to these Terms and Conditions."
                        "1. Use of Services"
                        "1.1 DocKo is designed to assist users in booking hospital and clinic appointments, managing health records, and receiving reminders."
                        "1.2 By using this app, you confirm that the information you provide is accurate and up-to-date.",
                        size=12,
                        color='#808080'
                    ),
                ]
            )

        elif step == 7:
            return ft.Column(
                [
                    ft.Text("Step 7: Final Confirmation", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                    ft.Text("Please review your information before submitting.", size=16, color=ft.Colors.BLUE),
                    ft.ElevatedButton("Submit Information", on_click=lambda e: print("Form submitted!"), bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
                ]
            )

    # Step container
    step_container = ft.Column()
    error_text = ft.Text(color=ft.Colors.RED, size=16)
    progress_bar = ft.ProgressBar(width=700, height=8, color=ft.Colors.BLUE, value=0.14)

    update_form()

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    progress_bar,
                    error_text,
                    step_container,
                    ft.Row(
                        [
                            ft.ElevatedButton("Previous", on_click=previous_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
                            ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
                        ] if current_step["value"] < 7 else [
                            ft.ElevatedButton("Submit", on_click=lambda e: print("Form submitted!"), bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ]
            ),
            width=700,
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.GREY_300, spread_radius=2),
        )
    )

ft.app(target=main)

import datetime
import flet as ft
import json
import os
from DocKoApp.pages.page.doctor_sign_in import DocSign
from DocKoApp.pages.page.home_page import HomePage

# Path to the JSON file where user data will be stored
DATA_FILE = "doctors.json"
file_picker = ft.FilePicker()
form_data = {}

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

def SignUp(page: ft.Page):

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

    # Variable to track the current step
    current_step = 0

    # Function to update the container with the current step
    def update_step():
        step_container.content = steps[current_step]
        step_container.update()

    # Navigation button handlers
    def next_step(e):
        nonlocal current_step
        if current_step < len(steps) - 1:
            current_step += 1
            update_step()

    def previous_step(e):
        nonlocal current_step
        if current_step > 0:
            current_step -= 1
            update_step()

    def build_form_step(step):
        pass

    def on_phone_number_change(e):
        # Allow only numeric characters
        if not e.control.value.isdigit():
            phone_number.error_text = "Only numbers are allowed"
            phone_number.value = ''.join(filter(str.isdigit, e.control.value))
        else:
            phone_number.error_text = None  # Clear the error message
        page.update()

    def on_postal_code_change(e):
        # Allow only digits
        if not e.control.value.isdigit():
            postal_code.error_text = "Only numbers are allowed"
            postal_code.value = ''.join(filter(str.isdigit, e.control.value))

        else:
            postal_code.error_text = None  # Clear any error message
        page.update()

    def on_checkbox_change(e):
        """Handle checkbox value changes."""
        checkbox_label = e.control.label
        if e.control.value:  # Checkbox checked
            selected_specializations.append(checkbox_label)
        else:  # Checkbox unchecked
            selected_specializations.remove(checkbox_label)
        update_result()

    def on_other_specialization_change(e):
        """Handle changes to the 'Other Specialization' text field."""
        nonlocal other_specialization
        other_specialization = e.control.value
        update_result()

    def update_result():
        """Update the result text with current selections."""
        result.value = f"Selected Specializations: {', '.join(selected_specializations)}"
        if other_specialization:
            result.value += f"\nOther Specialization: {other_specialization}"
        page.update()

    # Displays and Updates DOB based on the date picked.
    dob_display = ft.Container(
        ft.Text("Date of Birth: Not selected", size=16, color=ft.Colors.BLACK),
        border=ft.border.all(1, ft.Colors.BLUE),
        padding=6,
        margin=ft.margin.only(top=5, bottom=5),
        width=250,
    ),

    def update_dob(e):
        dob_display.content = ft.Text(f"Date of Birth: {form_data['dob'].strftime('%Y-%m-%d')}",
                                      color=ft.Colors.BLACK)  # Update display
        page.update()

    # Step container
    step_container = ft.Column()
    error_text = ft.Text(color=ft.Colors.RED, size=16)
    progress_bar = ft.ProgressBar(width=700, height=8, color=ft.Colors.BLUE, value=0.14)
    update_step()

    # Define the form fields
    # Step 1
    step_one = ft.Text("Step 1: Personal Information", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
    first_name = ft.TextField(label="First Name", border_color=ft.Colors.BLUE, color=ft.Colors.BLACK),
    middle_name = ft.TextField(label="Middle Name (Optional)", border_color=ft.Colors.BLUE, color=ft.Colors.BLACK),
    last_name = ft.TextField(label="Last Name", border_color=ft.Colors.BLUE, color=ft.Colors.BLACK),
    gender = ft.Dropdown(label="Gender",options=
    [
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
    phone_number = ft.TextField(label="Phone Number",border_color=ft.Colors.BLUE,
            keyboard_type=ft.KeyboardType.NUMBER,
            color=ft.Colors.BLACK,
            max_length=11,
            on_change=on_phone_number_change
    ),

    # Step 2
    country = ft.Dropdown(label="Country",options=[ft.dropdown.Option("Philippines")],
            border_color=ft.Colors.BLUE,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK),
    province = dropdown = ft.Dropdown(label="State/Province",options=
    [
                ft.dropdown.Option("Metro Manila"),
                ft.dropdown.Option("Central Visayas"),
                ft.dropdown.Option("Davao Region"),
                ft.dropdown.Option("Cordillera Administrative Region"),
                ft.dropdown.Option("Western Visayas"),
                ft.dropdown.Option("Northern Mindanao"),
                ft.dropdown.Option("CALABARZON"),
                ft.dropdown.Option("Bicol Region"),
                ft.dropdown.Option("Ilocos Region"),
                ft.dropdown.Option("Eastern Visayas"),
            ],
            border_color=ft.Colors.BLUE,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        ),
    city = ft.TextField(label="City",border_color=ft.Colors.BLUE,color=ft.Colors.BLACK),
    street = ft.TextField(label="Street Address",border_color=ft.Colors.BLUE,color=ft.Colors.BLACK),
    postal_code= ft.TextField(label="Postal Code",border_color=ft.Colors.BLUE,
            keyboard_type=ft.KeyboardType.NUMBER,
            max_length=4,  # Limit the postal code to 4 digits
            color=ft.Colors.BLACK,
            on_change=on_postal_code_change
    ),

    # Step 3-Specialization
    selected_specializations = []
    gp_checkbox = ft.Checkbox(label="General Practitioner (GP)", check_color=ft.Colors.BLUE,on_change=on_checkbox_change)
    dentist_checkbox = ft.Checkbox(label="Dentist", check_color=ft.Colors.BLUE, on_change=on_checkbox_change)
    psychiatrist_checkbox = ft.Checkbox(label="Psychiatrist", check_color=ft.Colors.BLUE, on_change=on_checkbox_change)
    dermatologist_checkbox = ft.Checkbox(label="Dermatologist", check_color=ft.Colors.BLUE,on_change=on_checkbox_change)
    obgyn_checkbox = ft.Checkbox(label="Obstetrician/Gynecologist", check_color=ft.Colors.BLUE,on_change=on_checkbox_change)
    other_specialization = ft.TextField(label="Other Specialization (Optional)",
        border_color=ft.Colors.BLUE,
        color=ft.Colors.BLACK,
        expand=True,
        on_change=on_other_specialization_change
    ),
    result = ft.Text(size=16, color=ft.Colors.BLACK)


    # Step 4
    title = ft.TextField(label="Your Title (e.g., RN, MD, DO, etc.)",
            border_color=ft.Colors.BLUE,
            color=ft.Colors.BLACK,
            expand=True,
    ),
    previous_hospitals = ft.TextField(label="Previous Hospitals/Clinics (Separate entries with commas)",
            border_color=ft.Colors.BLUE,
            color=ft.Colors.BLACK,
            multiline=True,
            expand=True,
    ),
    years_of_experience = ft.Slider(min=0,max=50,divisions=50,value=0,thumb_color=ft.Colors.BLUE,
            active_color=ft.Colors.LIGHT_BLUE,
            inactive_color='#000000',
            label="Years: {value}",
            autofocus=True,
    ),
    license_number = ft.TextField(label="License Number",border_color=ft.Colors.BLUE,
            keyboard_type=ft.KeyboardType.NUMBER,
            color=ft.Colors.BLACK,
            max_length=7,
            on_change=on_phone_number_change
    ),

    # Step 5
    profile_picture = ft.ElevatedButton("Upload Profile Picture (JPG, PNG)",
            on_click=lambda _: file_picker.pick_files(
            allow_multiple=False,
            allowed_extensions=["jpg", "png"]
            )
    ),

    buttons = ft.Row([
        ft.ElevatedButton("Previous", on_click=previous_step, bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE),
        ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE,
            color=ft.Colors.WHITE),
    ],alignment=ft.MainAxisAlignment.CENTER,
    ),

    def handle_sign_up(e):
        # Collect doctor data
        doctor_data = {
        "first_name": first_name.value,
        "middle_name": middle_name.value,
        "last_name": last_name.value,
        "dob": form_data['dob'],
        "gender": gender.value,
        "phone_number": phone_number.value,
        "license_number": license_number.value,
        "country": "Philippines",
        "state_province": province.value,
        "city": city.value,
        "street_address": street.value,
        "postal_code": postal_code.value,
        "specializations": [selected_specializations],
        "other_specialization": other_specialization.value,
        "title": title.value,
        "previous_hospitals": previous_hospitals.value,
        "years_of_experience": years_of_experience.value,
        "profile_picture": profile_picture.value,
    }

        # Load existing data
        doctors = load_data()
        # Append new user
        doctors.append(doctor_data)
        # Save updated data to JSON file
        save_data(doctors)

        # Clear input fields and show a success message
        page.views.append(HomePage(page))

    # Create a list of steps for easy management
    steps = [
        ft.Column([
            ft.Text("Step 1: Personal Information", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
            first_name,
            middle_name,
            last_name,
            dob_display,
            gender,
            phone_number,
            buttons
        ]), #Step 1
        ft.Column([
            ft.Text("Step 2: Contact Information", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
            country,
            province,
            city,
            street,
            postal_code,
            buttons
        ]), #Step 2
        ft.Column([
            ft.Text("Step 3: Specializations and Expertise",size=22,weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE),
            ft.Text("Please select your primary specializations and add any additional expertise.",size=16,color=ft.Colors.GREY),
            ft.Divider(color=ft.Colors.BLUE),
            gp_checkbox,
            dentist_checkbox,
            psychiatrist_checkbox,
            dermatologist_checkbox,
            obgyn_checkbox,
            other_specialization,
            buttons
        ], spacing=10), #Step 3
        ft.Column([
            ft.Text("Step 4: Professional Background",size=22,weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE),
            ft.Text("Provide details about your previous experience in hospitals, clinics, and your title.",size=16,color=ft.Colors.GREY),
            ft.Divider(color=ft.Colors.BLUE),
            title,
            previous_hospitals,
            ft.Text("Years of Experience in the Medical Field:",size=16,color=ft.Colors.BLACK),
            years_of_experience,
            buttons
        ], spacing=10),  # Step 4
        ft.Column([
            ft.Text("Step 5: Profile Picture",size=22,weight=ft.FontWeight.BOLD,color=ft.Colors.BLUE),
            ft.Text("Upload your profile picture (JPG, PNG) and resume (PDF).",size=16,color=ft.Colors.GREY),
            ft.Divider(color=ft.Colors.BLUE),
            profile_picture,
            ft.Row(
                [
                    ft.Text(
                        f"Selected file: {file_picker.result.files[0].name}" if file_picker.result else "No file selected")
                ],
                alignment=ft.MainAxisAlignment.START
            ),
            buttons
        ], spacing=15),  # Step 5
        ft.Column([
            ft.Text("Step 6: Privacy and Consent", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
            ft.Checkbox(label="I agree to the terms and conditions", check_color=ft.Colors.BLUE),
            ft.Checkbox(label="I consent to the collection and use of my health data",check_color=ft.Colors.BLUE),
            ft.Text(
                "Welcome to DocKo, your trusted healthcare appointment booking app. Please read these Terms and Conditions carefully before using our services. By registering for and using DocKo, you agree to these Terms and Conditions."
                "(1) Use of Services"
                "(1.1) DocKo is designed to assist users in booking hospital and clinic appointments, managing health records, and receiving reminders."
                "(1.2) By using this app, you confirm that the information you provide is accurate and up-to-date.",
                size=12,
                color='#808080'),
            buttons
        ]),  # Step 6
        ft.Column([
            ft.Text("Step 7: Final Confirmation", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
            ft.Text("Please review your information before submitting.", size=16, color=ft.Colors.BLUE),
            ft.Row([
                ft.ElevatedButton("Submit Information", on_click=handle_sign_up,
                                  bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)],
                alignment=ft.MainAxisAlignment.CENTER),
        ]),  # Step 7
    ]

    # Container to display the current step
    step_container = ft.Container(padding=10, content=steps[current_step])

    return ft.View(
        route="/docform",
        controls=[
            ft.Row(
                [
                    ft.Container(
                        content=ft.Row(
                            controls=[
                                ft.Image(
                                    src="assets/logo.png",
                                    width=175,
                                    height=175,
                                ),
                                ft.Text(
                                    "DocKo",
                                    size=90,
                                    color=ft.colors.BLUE,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ],
                            alignment="center",
                            spacing=10,
                        ),
                        height=500,
                        margin=10,
                    ),

                    # Empty column to push the container to the right
                    ft.Column([], expand=True),

                    # Container positioned at the right middle
                    ft.Container(
                        ft.Column(
                            [
                                progress_bar,
                                error_text,
                                step_container,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        width=700,
                        padding=20,
                        margin=20,
                        border_radius=10,
                        bgcolor=ft.Colors.WHITE,
                        shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.GREY_300, spread_radius=2),
                    ),
                ],
            ),
        ]
    ),




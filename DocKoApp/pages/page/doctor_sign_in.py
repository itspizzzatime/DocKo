import flet as ft
import datetime
import json
from DocKoApp.pages.page.home_page import HomePage

def DocSign(page):
    page.bgcolor = ft.Colors.LIGHT_BLUE_50

    def upload_file(event):
        if event.files:  # Check if files were selected
            file = event.files[0]  # Get the first uploaded file
            image_path = file.path  # Get the path of the uploaded file
            image_display.src = image_path  # Update the Image widget source
        else:
            image_display.src = ""  # Reset the image display if no file selected
        page.update()

    # Navigation between steps
    current_step = {"value": 1}
    form_data = {}
    # Define the form fields
    # Step 1
    step_one = ft.Text("Step 1: Personal Information", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
    first_name = ft.TextField(label="First Name", value=form_data.get("First Name", ""),border_color=ft.Colors.BLUE,)
    middle_name = ft.TextField(label="Middle Name (Optional)", value=form_data.get("Middle Name (Optional)", ""),border_color=ft.Colors.BLUE,)
    last_name = ft.TextField(label="Last Name", value=form_data.get("Last Name", ""),border_color=ft.Colors.BLUE,)
    age= ft.TextField(label="Age", border_color=ft.Colors.BLUE,
                                keyboard_type=ft.KeyboardType.NUMBER,
                                color=ft.Colors.BLACK,
                                value=form_data.get("Age", ""),
                                max_length=2,
    )
    gender = ft.Dropdown(label="Gender", options=
    [
        ft.dropdown.Option("Male"),
        ft.dropdown.Option("Female"),
        ft.dropdown.Option("Non-Binary"),
        ft.dropdown.Option("Prefer not to say"),
        ft.dropdown.Option("Other"),
    ],
         border_color=ft.Colors.BLUE,
         value=form_data.get("Gender"),
         bgcolor=ft.Colors.WHITE,
         color=ft.Colors.BLACK,
    )

    # Step 2
    step_two = ft.Text("Step 2: Contact Information", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
    phone_number = ft.TextField(label="Phone Number", border_color=ft.Colors.BLUE,
                                keyboard_type=ft.KeyboardType.NUMBER,
                                color=ft.Colors.BLACK,
                                max_length=11,
                                value=form_data.get("Phone Number", "")
    )
    email = ft.TextField(label="Email", value=form_data.get("Email", ""),border_color=ft.Colors.BLUE)
    soc_med = ft.TextField(label="Social Media Links", value=form_data.get("Social Media Links", ""),border_color=ft.Colors.BLUE)

    # Step 3
    step_three = ft.Text("Step 3: Workplace Adress", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
    country = ft.Dropdown(label="Country", options=[ft.dropdown.Option("Philippines")],
                          border_color=ft.Colors.BLUE,
                          bgcolor=ft.Colors.WHITE,
                          value=form_data.get("Country", ""),
                          color=ft.Colors.BLACK,
    )
    province = dropdown = ft.Dropdown(label="State/Province", options=
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
                                      value=form_data.get("Country", ""),
                                      )
    city = ft.TextField(label="City", border_color=ft.Colors.BLUE, color=ft.Colors.BLACK,value=form_data.get("City", ""),)
    street = ft.TextField(label="Street Address", border_color=ft.Colors.BLUE, color=ft.Colors.BLACK,value=form_data.get("Street", ""),)
    postal_code = ft.TextField(label="Postal Code", border_color=ft.Colors.BLUE,
                               keyboard_type=ft.KeyboardType.NUMBER,
                               max_length=4,  # Limit the postal code to 4 digits
                               color=ft.Colors.BLACK,
                               value=form_data.get("Postal Code", ""),
                               )

    # Step 4-Specialization
    field_specialization = ft.TextField(label="Primary Field Specialization",
                                        border_color=ft.Colors.BLUE,
                                        color=ft.Colors.BLACK,
                                        expand=True,
                                        value=form_data.get("Primary Field Specialization", ""),
                                        )
    field_specialization_secondary = ft.TextField(label="Secondary Field Specialization",
                                        border_color=ft.Colors.BLUE,
                                        color=ft.Colors.BLACK,
                                        expand=True,
                                        value=form_data.get("Secondary Field Specialization", ""),
                                        )

    result = ft.Text(size=16, color=ft.Colors.BLACK)

    # Step 5
    title = ft.TextField(label="Your Title (e.g., RN, MD, DO, etc.)",
                         border_color=ft.Colors.BLUE,
                         color=ft.Colors.BLACK,
                         expand=True,
                         value=form_data.get("Title", ""),
                         )
    previous_hospitals = ft.TextField(label="Affiliated Hospitals/Clinics (Separate entries with commas)",
                                      border_color=ft.Colors.BLUE,
                                      color=ft.Colors.BLACK,
                                      multiline=True,
                                      expand=True,
                                      value=form_data.get("Affiliated Hospitals", ""),
                                      )
    years_of_experience = ft.TextField(label="Years of Experience", border_color=ft.Colors.BLUE,
                                  keyboard_type=ft.KeyboardType.NUMBER,
                                  color=ft.Colors.BLACK,
                                  max_length=2,
                                  value=form_data.get("Years of Experience", ""),
                                  )

    license_number = ft.TextField(label="License Number", border_color=ft.Colors.BLUE,
                                  keyboard_type=ft.KeyboardType.NUMBER,
                                  color=ft.Colors.BLACK,
                                  max_length=7,
                                  value=form_data.get("License Number", ""),
                                  )

    # Step 6
    image_display =ft.Image(
            src="DocKoApp/assets/icons/placeholder-profile.png",  # Placeholder URL
            width=128,
            height=128,
            border_radius=64
    )


    # File Picker for uploading images
    file_picker = ft.FilePicker(on_result=upload_file)
    file_picker.accept = "image/jpeg,image/png"  # Accept only JPEG and PNG images
    page.overlay.append(file_picker)  # Add FilePicker to page.overlay

    profile_picture = ft.ElevatedButton("Upload Profile Picture (JPG, PNG)",
                                        on_click=lambda _: file_picker.pick_files(
                                            allow_multiple=False,
                                            allowed_extensions=["jpg", "png"]
                                        ),

                                        )

    availability = ft.Dropdown(label="Availability", options=
    [
        ft.dropdown.Option("Online Consultation"),
        ft.dropdown.Option("In-Person Consultation"),
        ft.dropdown.Option("Both"),
    ],
                         border_color=ft.Colors.BLUE,
                         value=form_data.get("Availability"),
                         bgcolor=ft.Colors.WHITE,
                         color=ft.Colors.BLACK,
    )

    rates = ft.TextField(label="Rate", border_color=ft.Colors.BLUE,
                                keyboard_type=ft.KeyboardType.NUMBER,
                                color=ft.Colors.BLACK,
                                max_length=4,
                                value=form_data.get("Rate", "")
    )

    schedule = ft.TextField(label="Schedule for Consultation *Ex. (7:00 AM - 9:00 PM)",
                         border_color=ft.Colors.BLUE,
                         color=ft.Colors.BLACK,
                         expand=True,
                         value=form_data.get("Schedule", ""),
    )


    # Validation function
    def validate_inputs():
        current_controls = step_container.controls[0].controls
        checkbox_checked = False

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
                    checkbox_checked = True
            if isinstance(control, ft.Dropdown) and not control.value and "Optional" not in control.label:
                error_text.value = "Please select an option from the dropdown."
                return False
            if isinstance(control, ft.DatePicker) and "dob" not in form_data:
                error_text.value = "Please pick a date."
                return False

        if any(isinstance(control, ft.Checkbox) for control in current_controls) and not checkbox_checked:
            error_text.value = "Please check at least one required box."
            return False

        return True

    def save_form_data():
        with open("form_data.json", "w") as file:
            json.dump(form_data, file, indent=4, default=str)

    def next_step(e):
        if not validate_inputs():
            page.update()
            return

        save_current_step_data()

        if current_step["value"] < 8:
            current_step["value"] += 1
            update_form()

    def previous_step(e):
        save_current_step_data()

        if current_step["value"] > 1:
            current_step["value"] -= 1
            update_form()

    def save_current_step_data():
        current_controls = step_container.controls[0].controls

        for control in current_controls:
            if isinstance(control, ft.TextField):
                form_data[control.label] = control.value
            elif isinstance(control, ft.Dropdown):
                form_data[control.label] = control.value
            elif isinstance(control, ft.Checkbox):
                form_data[control.label] = control.value

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
        form_data["Date of Birth"] = e.control.value
        dob_display.content = ft.Text(f"Date of Birth: {form_data['Date of Birth'].strftime('%Y-%m-%d')}",color=ft.Colors.BLACK)  # Update display
        page.update()

    f_names = [doctor['First Name'] for doctor in form_data]
    l_ames = [doctor['Last Name'] for doctor in form_data]
    specialization = [doctor['Primary Field Specialization'] for doctor in form_data]
    experience = [doctor['Experience'] for doctor in form_data]
    availabilities = [doctor['Availability'] for doctor in form_data]
    price_raet = [doctor['Rate'] for doctor in form_data]
    sched = [doctor['Schedule'] for doctor in form_data]
    hospital = [doctor['Affiliated Hospitals'] for doctor in form_data]
    pf = [doctor['Profile Picture'] for doctor in form_data]

    def load_form_data(step):
        if step == 1:
            controls = [
                step_one,
                first_name,
                middle_name,
                last_name,
                age,
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
                gender,
                ft.Row([
                    ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE),
                ],alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls
        elif step == 2:
            controls = [
                step_two,
                phone_number,
                email,
                soc_med,
                ft.Row([
                    ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls
        elif step == 3:
            controls = [
                step_three,
                country,
                province,
                city,
                street,
                postal_code,
                ft.Row([
                    ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls
        elif step == 4:
            controls = [
                ft.Text(
                    "Step 4: Specializations and Expertise",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE
                ),
                ft.Text(
                    "Please select your primary specializations and add any additional expertise.",
                    size=16,
                    color=ft.Colors.GREY
                ),
                ft.Divider(color=ft.Colors.BLUE),
                field_specialization,
                field_specialization_secondary,
                ft.Row([
                    ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls
        elif step == 5:
            controls = [
                ft.Text("Step 4: Professional Background",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE
                        ),
                ft.Text("Provide details about your previous experience in hospitals, clinics, and your title.",
                        size=16,
                        color=ft.Colors.GREY
                        ),
                ft.Divider(color=ft.Colors.BLUE),
                title,
                previous_hospitals,
                years_of_experience,
                license_number,
                ft.Row([
                    ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            form_data["Years of Experience"] = years_of_experience.value,
            return controls
        elif step == 6:
            controls = [
                ft.Text(
                    "Step 5: Profile Setup",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE
                ),
                ft.Text(
                    "Upload your profile picture (JPG, PNG) and resume (PDF).",
                    size=16,
                    color=ft.Colors.GREY
                ),
                ft.Divider(color=ft.Colors.BLUE),
                profile_picture,
                # Optional: File picker display for better feedback
                ft.Text("Selected files will appear here after upload."),
                ft.Row([
                    image_display
                ], alignment=ft.MainAxisAlignment.CENTER
                ),
                availability,
                rates,
                schedule,
                ft.Row([
                    ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls
        elif step == 7:
            controls = [
                ft.Text("Step 7: Privacy and Consent", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
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
                ft.Row([
                    ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls
        elif step == 8:
            controls = [
                ft.Text("Step 8: Final Confirmation", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                ft.Text("Please review your information before submitting.", size=16, color=ft.Colors.BLUE),
                ft.Divider(color=ft.Colors.BLUE),
                ft.Row([
                    image_display
                ], alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Column(
                    [
                        ft.Column(
                            [
                                ft.Column([
                                    ft.Text(f"{key}:", weight="bold", size=18, no_wrap=False),
                                ], alignment=ft.MainAxisAlignment.START),
                                ft.Column([
                                    ft.Text(f"       {value}", size=14),
                                ], alignment=ft.MainAxisAlignment.CENTER),
                            ],
                        )
                        for key, value in form_data.items()
                    ],
                    spacing=5,
                ),
                ft.Row([
                    ft.ElevatedButton("Submit Information", on_click=submit_form, bgcolor=ft.Colors.BLUE,color=ft.Colors.WHITE),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls




    def update_form():
        error_text.value = ""
        progress_bar.value = current_step["value"] / 8
        step_container.controls.clear()
        step_container.controls.append(ft.Column(load_form_data(current_step["value"])))
        page.update()

    def submit_form(e):
        save_current_step_data()
        save_form_data()
        page.go("/home")

    step_container = ft.Column()
    error_text = ft.Text(color=ft.Colors.RED, size=16)
    progress_bar = ft.ProgressBar(width=700, height=8, color=ft.Colors.BLUE, value=0.14)

    update_form()

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
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            spacing=10,
                        ),
                        margin=10
                    ),
                    ft.Column([], expand=True),
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
                vertical_alignment=ft.CrossAxisAlignment.START
            )

        ],
        scroll="adaptive"
    )


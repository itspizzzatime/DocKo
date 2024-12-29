import flet as ft
import datetime
import json

def ClientSign(page):
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
    step_three = ft.Text("Step 3: State Symptoms and Experiences", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE)
    symptoms = ft.TextField(
        label="Symptoms",
        border_color=ft.Colors.BLUE,
        bgcolor=ft.Colors.WHITE,
        color=ft.Colors.BLACK,
        max_lines=10,  # Maximum number of lines before scrolling
        height=100,  # Height of the text field
        multiline=True,  # Enables multi-line input
        value=form_data.get("Symptoms", "")
    )

    # Step 4
    image_display =ft.Image(
            src="DocKoApp/assets/icons/placeholder-profile.png",  # Placeholder URL
            width=128,
            height=128,
    )

    # File Picker for uploading images
    file_picker = ft.FilePicker(on_result=upload_file)
    file_picker.accept = "image/jpeg,image/png"  # Accept only JPEG and PNG images
    page.overlay.append(file_picker)  # Add FilePicker to page.overlay

    supporting_images = ft.ElevatedButton("Upload Profile Picture (JPG, PNG)",
                                        on_click=lambda _: file_picker.pick_files(
                                            allow_multiple=False,
                                            allowed_extensions=["jpg", "png"]
                                        ),)
    # Step 5: Payment

    card_num = ft.TextField(label="Card Number", border_color=ft.Colors.BLUE,
                                keyboard_type=ft.KeyboardType.NUMBER,
                                color=ft.Colors.BLACK,
                                max_length=16,
                                value=form_data.get("Card Number", "")
    )

    expiry_date = ft.TextField(label="Expiry Date", border_color=ft.Colors.BLUE,
                            keyboard_type=ft.KeyboardType.NUMBER,
                            color=ft.Colors.BLACK,
                            max_length=5,
                            value=form_data.get("Expiry Date", "")
                            )

    cvv = ft.TextField(label="CVV", border_color=ft.Colors.BLUE,
                            keyboard_type=ft.KeyboardType.NUMBER,
                            color=ft.Colors.BLACK,
                            max_length=3,
                            value=form_data.get("CVV", "")
                            )

    qr_display = ft.Image(
        src="DocKoApp/assets/icons/placeholder-profile.png",  # Placeholder URL
        width=128,
        height=128,
        border_radius=64
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

        if current_step["value"] < 7:
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

    # client_booking.py
    def navigate_to_home_page():
        from DocKoApp.pages.page.home_page import HomePage
        return HomePage()

    def load_form_data(step):
        if step == 1:
            controls = [
                step_one,
                first_name,
                middle_name,
                last_name,
                age,
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
                symptoms,
                ft.Row([
                    ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls
        elif step == 4:
            controls = [
                ft.Text(
                    "Step 4: Upload any images that might support the consultation",
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
                supporting_images,
                # Optional: File picker display for better feedback
                ft.Text("Selected files will appear here after upload."),
                ft.Row([
                    image_display
                ], alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row([
                    ft.ElevatedButton("Next", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls
        elif step == 5:
            controls = [
                ft.Text("Step 5: Payment", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                ft.Column([
                   ft.Column([
                       ft.Text(
                           "Enter the following bank details for Bank transaction.",
                           size=16,
                           color=ft.Colors.GREY
                       ),
                       card_num,
                       expiry_date,
                       cvv,
                   ]),
                    ft.Column([
                        ft.Text(
                            "GCash and other E-wallets",
                        ),
                        ft.Image(
                            src=r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\qr.png",  # Placeholder URL
                            width=128,
                            height=128,
                        )
                    ]),
                ]),
                ft.Row([
                    ft.ElevatedButton("Submit Details", on_click=next_step, bgcolor=ft.Colors.BLUE, color=ft.Colors.WHITE)
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls
        elif step == 6:
            controls = [
                ft.Text("Step 5: Privacy and Consent", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
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
        elif step == 7:
            controls = [
                ft.Text("Thank you for booking with us!", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE),
                ft.Divider(color=ft.Colors.BLUE),
                ft.Row([
                    ft.ElevatedButton("Back to Home", on_click=submit_form, bgcolor=ft.Colors.BLUE,color=ft.Colors.WHITE),
                ], alignment=ft.MainAxisAlignment.CENTER)
            ]
            return controls


    def update_form():
        error_text.value = ""
        progress_bar.value = current_step["value"] / 7
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


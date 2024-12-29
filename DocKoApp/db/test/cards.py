import flet as ft

# Function to create a doctor card
def create_doctor_card(name, specialization, experience, online, in_person, schedule, fee, hospital, images, on_book):
    return ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Image(src=images, width=64, height=64, border_radius=32),
                        ft.Column(
                            [
                                ft.Text(name, weight="bold", size=16),
                                ft.Text(specialization, size=14, color="gray"),
                                ft.Text(f"{experience} yrs experience", size=12, color="gray"),
                            ],
                            spacing=2,
                        ),
                    ],
                    spacing=10,
                ),
                ft.Row(
                    [
                        ft.Text("✔ Online Consultation" if online else "❌ Online Consultation", size=12),
                        ft.Text("✔ In-Person Consultation" if in_person else "❌ In-Person Consultation", size=12),
                    ],
                    spacing=10,
                ),
                ft.Row(
                    [
                        ft.Column(
                            [
                                ft.Text("Earliest Available Schedule", weight="bold", size=14),
                                ft.Text(hospital, size=12),
                                ft.Text(schedule, size=12, color="gray"),
                                ft.Text(f"Fee: {fee}" if fee else "Fee: -", size=12, color="gray"),
                            ],
                        ),
                        ft.Container(width=20),  # Spacer replacement
                        ft.Column(
                            [
                                ft.ElevatedButton(
                                    "BOOK APPOINTMENT", on_click=on_book, bgcolor="blue", color="white"
                                ),
                                ft.ElevatedButton(
                                    "VIEW PROFILE", bgcolor="lightblue", color="white"
                                ),
                            ],
                            spacing=5,
                        ),
                    ],
                    alignment="spaceBetween",
                ),
            ],
            spacing=10,
            scroll="adaptive"
        ),
        padding=15,
        border=ft.border.all(1, color="lightgray"),
        border_radius=8,
        margin=ft.margin.only(top=10),
    )

# Function to build the list of doctor cards
def build_doctor_cards(page, doctors, on_book_appointment):
    return ft.Column(
        spacing=15,
        expand=True,
        controls=[
            create_doctor_card(*doctor, on_book_appointment) for doctor in doctors
        ],
        horizontal_alignment="center",
    )

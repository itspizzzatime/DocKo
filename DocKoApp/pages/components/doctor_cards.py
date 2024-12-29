import flet as ft
from DocKoApp.pages.page.client_booking import ClientSign

def create_doctor_card(name, specialization, experience, online, in_person, schedule, fee, hospital, images, on_book):
    return ft.Container(
        content=ft.Column(
            [
                # Doctor Name and Specialization
                ft.Row(
                    [
                        ft.Image(
                            src=images,  # Placeholder image
                            width=64,
                            height=64,
                            border_radius=32,
                        ),
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
                # Consultation Options
                ft.Row(
                    [
                        ft.Text("✔ Online Consultation" if online else "❌ Online Consultation", size=12),
                        ft.Text("✔ In-Person Consultation" if in_person else "❌ In-Person Consultation", size=12),
                    ],
                    spacing=10,
                ),
                # Schedule and Fees
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
                                    "BOOK APPOINTMENT",
                                    on_click=on_book,
                                    bgcolor="blue",
                                    color="white",
                                ),
                                ft.ElevatedButton(
                                    "VIEW PROFILE",
                                    bgcolor="lightblue",
                                    color="white",
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

def build_doctor_cards(page):
    def on_book_appointment(e):
        page.route = "/book"
        page.update()

    doctors = [
        ("Dr. Paula Glenn Salamante", "Dentist - General Dentistry", "15", True, True, "Tomorrow, 03:00 PM - 05:00 PM",
         "₱700.00", "Delos Santos Medical Center RM",
         r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\doctor_image\Dr. Paula Glenn Salamante.jpg"),
        ("Dr. Keziah Christabel Aquino", "Doctor of Dental Medicine - General Dentistry", "15", True, True,
         "Tomorrow, 03:00 PM - 05:00 PM", "₱700.00", "Delos Santos Medical Center RM",
         r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\doctor_image\Dr. Keziah Christabel Aquino.jpg"),
        ("Dr. Alberto Adrales", "MD, FPDS - Dermatology", "15", True, True, "Tomorrow, 03:00 PM - 05:00 PM", "₱700.00",
         "Delos Santos Medical Center RM",
         r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\doctor_image\Dr. Alberto Adrales.jpg"),
        ("Dr. Veronica Therese Villanueva", "MD, MHA, PhD - Ophthalmology", "15", True, True,
         "Tomorrow, 03:00 PM - 05:00 PM", "₱700.00", "Delos Santos Medical Center RM",
         r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\doctor_image\Dr. Veronica Therese Villanueva.jpg"),
        ("Dr. Emelito Galeos", " RN, MD - Obstetrician-Gynecology - Reproductive Health", "3", False, True,
         ", 07:00 AM - 10:00 PM", "₱400.00", "University of Santo Tomas Hospital",
         r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\doctor_image\Dr. Mark McKelvie.jpg"),
        ("Dr. Lora Grace Deles", "MD, FPCP, DPSMID	Infectious Diseases	Public Health and Infection Control", "8",
         True, True, "Tomorrow, 03:00 PM - 05:00 PM", "₱700.00", "Delos Santos Medical Center RM",
         r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\doctor_image\Dr. Andre Agoncillo.jpg"),
        ("Dr. Myvie Galon", "MD	Infectious Diseases	Internal Medicine", "10", True, True,
         "Tomorrow, 03:00 PM - 05:00 PM", "₱700.00", "Delos Santos Medical Center RM",
         r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\doctor_image\Dr. Myvie Galon.jpg"),
        ("Dr. Marron Francia", "RN-Internal Medicine-Cardiology", "12", False,
         True, "6:00 AM - 9:00 AM", "₱500.00", "UST Hospital", r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\doctor_image\Dr. Jan Jorge Francisco.jpg"),
        ("Dr. Anna Celinna Velenzuela", "MD, DPPS	General Pediatrics", "9", True, True,
         "Tomorrow, 03:00 PM - 05:00 PM", "₱700.00", "Delos Santos Medical Center RM",
         r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\doctor_image\Dr. Anna Celinna Valenzuela.jpg")
    ]

    return ft.Column(
        spacing=15,
        expand=True,
        controls=[
            create_doctor_card(name, specialization, experience, online, in_person, schedule, fee, hospital, images, on_book_appointment)
            for name, specialization, experience, online, in_person, schedule, fee, hospital, images in doctors
        ],
        horizontal_alignment="center",
    )


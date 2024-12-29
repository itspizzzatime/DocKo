import flet as ft
from DocKoApp.pages.components.headers import headerPage
from DocKoApp.pages.components.navbar import create_navbar



def ProfilePage(page, user_data:dict):
    def upload_file(event):
        if event.files:  # Check if files were selected
            file = event.files[0]  # Get the first uploaded file
            image_path = file.path  # Get the path of the uploaded file
            image_display.src = image_path  # Update the Image widget source
        else:
            image_display.src = ""  # Reset the image display if no file selected
        page.update()

    image_display = ft.Row([
        ft.Image(
            src=r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\icons\placeholder-profile.png",  # Placeholder URL
            width=128,
            height=128,
            border_radius=64,
        )
    ], alignment=ft.MainAxisAlignment.CENTER)

    # File Picker for uploading images
    file_picker = ft.FilePicker(on_result=upload_file)
    file_picker.accept = "image/jpeg,image/png"  # Accept only JPEG and PNG images
    page.overlay.append(file_picker)  # Add FilePicker to page.overlay

    def edit_form(e):
        page.views.append(
            ft.View(
                "/edit_form",
                bgcolor=ft.Colors.LIGHT_BLUE_50,
                controls=[
                    ft.Text("Edit User Information", size=24, weight=ft.FontWeight.BOLD, color="BLUE"),
                    ft.TextField(label="First Name", value=user_data.get("first_name", ""), color="black"),
                    ft.TextField(label="Middle Name", value=user_data.get("middle_name", ""), color="black"),
                    ft.TextField(label="Last Name", value=user_data.get("last_name", ""), color="black"),
                    ft.TextField(label="Age", value=str(user_data.get("age", "")), color="black"),
                    ft.TextField(label="Gender", value=user_data.get("gender", ""), color="black"),
                    ft.TextField(label="Email", value=user_data.get("email", ""), color="black"),
                    ft.TextField(label="Phone Number", value=user_data.get("phone", ""), color="black"),
                    ft.TextField(label="Address", value=user_data.get("address", ""), color="black"),
                    ft.ElevatedButton("Upload Profile Picture", on_click=file_picker.pick_files(allow_multiple=False,allowed_extensions=["jpg", "png"]),),
                    ft.ElevatedButton("Save", on_click=lambda e: page.go("/")),
                ],
            )
        )
        page.go("/edit_form")

    profile_picture = ft.Container(
        content=ft.Image(
            src=user_data.get("profile_picture", "default_user.png"),
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(50),
            width=350,
            height=350,
        ),
        alignment=ft.alignment.center,
        padding=10,
    )

    # Profile Picture Container
    profile_picture = ft.Container(
        content=ft.Image(
            src=r"C:\Users\PC\Downloads\DocKo\DocKoApp\assets\icons\placeholder-profile.png",
            fit=ft.ImageFit.COVER,
            border_radius=ft.border_radius.all(50),
            width=350,
            height=350,
        ),
        alignment=ft.alignment.center,
        padding=10,
    )

    # Details Section with White Background
    details = ft.Container(
        content=ft.Column(
            [
                ft.Text(
                    f"Name: {user_data.get('first_name', '')} {user_data.get('middle_name', '')} {user_data.get('last_name', '')}",
                    size=35,
                    weight=ft.FontWeight.BOLD,
                    color="black",
                ),
                ft.Text(f"Age: {user_data.get('age', 'N/A')}", color="black", size=30),
                ft.Text(f"Gender: {user_data.get('gender', 'N/A')}", color="black", size=30),
                ft.Text(f"Email: {user_data.get('email', 'N/A')}", color="black", size=30),
                ft.Text(f"Phone: {user_data.get('phone', 'N/A')}", color="black", size=30),
                ft.Text(f"Address: {user_data.get('address', 'N/A')}", color="black", size=30),
                ft.ElevatedButton(
                    content=ft.Text("Edit Information", size=30),  # Larger text size
                    on_click=edit_form,
                    bgcolor=ft.Colors.BLUE,
                    color=ft.Colors.WHITE,
                    width=250,
                ),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor="white",  # White background
        padding=20,
        border_radius=ft.border_radius.all(15),  # Optional rounded corners
        alignment=ft.alignment.center,
    )

    # Combine Profile Picture and Details in a Vertical Layout
    layout = ft.Column(
        [
            profile_picture,
            details,
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    profile_layout = ft.Row(
        [
            profile_picture,
            ft.Container(content=details, padding=10),
        ],
        spacing=50,
        alignment=ft.MainAxisAlignment.CENTER,
    )
    navbar = create_navbar(page)

    return ft.View(
        route="/profile",
        navigation_bar=navbar,
        controls=[
            ft.Row(
                [headerPage()],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,  # Spread out items
                vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Center items vertically
            ),
            ft.Row([
                profile_layout
            ], alignment=ft.MainAxisAlignment.CENTER)
        ],
    )






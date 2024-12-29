import flet as ft
from datetime import datetime, timedelta

def mode(page):
    msg = ft.AlertDialog(
        modal=False,
        title=ft.Row([ft.Text("Message", color=ft.colors.BLUE, weight=ft.FontWeight.BOLD, )],
                     alignment=ft.MainAxisAlignment.CENTER),
        content=ft.Column(
            [
                ft.Text(
                    "Ashley Cornejo - 19 - Female - Coughing, Runny nose, Runny eyes, Difficulty breathing,Itchiness, Rashes, Back Pain, - 0909123456789")
            ],
            height=175
        ),
        inset_padding=50,
    )

    return msg

def create_notification_card(title, message, time_elapsed):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text(title, weight="bold", size=18, color=ft.colors.BLUE_900),
                ft.Text(message, size=14, color=ft.colors.BLUE_GREY_600,),
                ft.Text(time_elapsed, size=12, color=ft.colors.BLUE_GREY_400, italic=True),
            ],
            width=1200,
            spacing=10,
            scroll="adaptive",
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        padding=15,
        border=ft.border.all(1, color="lightgray"),
        border_radius=8,
        margin=ft.margin.only(top=10),
        on_click=mode
    )



# Generate dynamic timestamps and time elapsed
now = datetime.now()
notifications = [
    ("Session Booked!", "Ashley Cornejo booked a session with you!", now - timedelta(minutes=1)),
    ("Update Available", "Version 2.1 is ready to download.", now - timedelta(minutes=1)),
    ("System Alert", "Your account password was changed successfully.", now - timedelta(minutes=1)),
]

def format_time_elapsed(notification_time):
    elapsed = now - notification_time
    if elapsed.days > 0:
        return f"{elapsed.days} day(s) ago"
    elif elapsed.seconds >= 3600:
        return f"{elapsed.seconds // 3600} hour(s) ago"
    elif elapsed.seconds >= 60:
        return f"{elapsed.seconds // 60} minute(s) ago"
    else:
        return "Just now"

notification_card = ft.Column(
        spacing=15,
        expand=True,
        controls=[
            create_notification_card(title, message, format_time_elapsed(time)) for title, message, time in
            notifications
        ],
        horizontal_alignment="center",
    )

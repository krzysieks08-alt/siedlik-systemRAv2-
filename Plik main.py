import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(
        ft.Container(
            content=ft.Text("SIEDLIK SYSTEM: AKTYWNY", size=30, weight="bold"),
            alignment=ft.alignment.center
        )
    )

ft.app(target=main)

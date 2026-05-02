import flet as ft

def main(page: ft.Page):
    page.title = "SIEDLIK SYSTEM"
    page.theme_mode = ft.ThemeMode.DARK
    page.add(ft.Text("SYSTEM DZIAŁA!", size=30))
    page.add(ft.ElevatedButton("GENERUJ SYGNAŁ"))

if __name__ == "__main__":
    ft.app(target=main)

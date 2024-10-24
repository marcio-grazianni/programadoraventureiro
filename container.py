import flet as ft


def main(page: ft.Page):
    container = ft.Container(
        margin=ft.margin.all(0),
        padding=ft.padding.all(0),
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#FCE7F3", "#E8D5FF"],
        ),
    )

    page.add(container)


if __name__ == "__main__":
    ft.app(target=main)

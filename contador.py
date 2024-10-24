import flet as ft

text_number = ft.TextField(
    value="0", text_align=ft.TextAlign.CENTER, width=100, read_only=True
)


def main(page: ft.Page):
    page.title = "Contador"
    page.window.height = 300
    page.window.width = 600
    page.window.alignment = ft.alignment.center
    page.bgcolor = ft.colors.PURPLE_300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    container1 = ft.Container(
        content=ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.REMOVE,
                    icon_color=ft.colors.WHITE,
                    on_click=minus_click,
                ),
                text_number,
                ft.IconButton(
                    icon=ft.icons.ADD, icon_color=ft.colors.WHITE, on_click=plus_click
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        bgcolor=ft.colors.PURPLE_700,
        border_radius=10,
        padding=30,
        width=300,
    )
    container2 = ft.Container(
        content=ft.Text(
            value="Desenvolvido por Marcio",
            text_align=ft.TextAlign.CENTER,
            size=15,
            weight=ft.FontWeight.BOLD,
        ),
        bgcolor=ft.colors.PURPLE_400,
        width=300,
        padding=ft.padding.all(5),
        border_radius=10,
    )

    page.add(container1, container2)


def minus_click(e):
    text_number.value = str(int(text_number.value) - 1)
    text_number.update()


def plus_click(e):
    text_number.value = str(int(text_number.value) + 1)
    text_number.update()


if __name__ == "__main__":
    ft.app(target=main)

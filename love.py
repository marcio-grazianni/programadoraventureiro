import flet as ft


def main(page: ft.Page):
    page.title = "Love"
    page.window.maximized = True
    page.bgcolor = "#030D21"
    page.window.max_width = 1100
    page.padding = ft.padding.all(0)

    header = ft.Container(
        col=12,
        margin=ft.margin.only(top=16),
        content=ft.ResponsiveRow(
            controls=[
                ft.Row(
                    col=8,
                    # expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Image(src="images/heart.png", height=32, width=32),
                        ft.Text("Love and Youu", color=ft.colors.WHITE, size=16, weight=ft.FontWeight.BOLD),
                    ]
                ),
                ft.Row(
                    col=4,
                    # expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton("Entrar", color=ft.colors.PRIMARY),
                        ft.ElevatedButton("Cadastre-se", color=ft.colors.SECONDARY),
                    ]
                ),
            ],
        ),
    )

    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            header,
        ],
    )

    page.add(layout)

    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")

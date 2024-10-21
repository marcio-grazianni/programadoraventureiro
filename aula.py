import flet as ft


def main(page: ft.Page):
    page.padding = ft.padding.all(32)
    page.bgcolor = ft.colors.WHITE

    row1 = ft.Container(
        bgcolor=ft.colors.BLUE,  # Definindo a cor de fundo como azul
        padding=10,  # Opcional: adicionando padding ao redor dos botões
        expand=True,
        border_radius=10,
        content=ft.Row(
            controls=[
                ft.ElevatedButton(text="1", bgcolor=ft.colors.RED, color=ft.colors.WHITE),
                ft.ElevatedButton(text="2", bgcolor=ft.colors.RED, color=ft.colors.WHITE),
                ft.ElevatedButton(text="3", bgcolor=ft.colors.RED, color=ft.colors.WHITE),
            ],
            # wrap=True,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            
        )
    )

    page.add(row1)

if __name__ == "__main__":
    ft.app(target=main)

import flet as ft


def main(page: ft.Page):
    page.title = "Jogo da Forca"
    page.bgcolor = ft.colors.BROWN_600

    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")

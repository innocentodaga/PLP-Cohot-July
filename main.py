import flet


def main(page: flet.Page):
    page.window.width = 320
    page.window.height = 600
    page.bgcolor = "#6e8383"
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    page.add(
        flet.Text("Hello World"),
        flet.TextButton("Tyson")
    )   


flet.app(main)
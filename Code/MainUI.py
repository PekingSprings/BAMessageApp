import flet as ft

def main(page: ft.Page):
    page.title="BAMessage"
    page.padding=0


    left_panel = ft.Container(
        content=ft.Text("左边导航", size=20, color=ft.Colors.BLACK),
        width=200,  # 固定宽度
        bgcolor=ft.Colors.GREY_300,  # 灰色背景
        alignment=ft.alignment.Alignment.CENTER,  # 让文字居中
    )

# 2. 右边：就是一个白色方块，里面写个“右”
    right_panel = ft.Container(
        content=ft.Text("右边聊天区", size=20),
        bgcolor=ft.Colors.WHITE,
        alignment=ft.alignment.Alignment.CENTER,
        expand=True,
    )
    row_layer=ft.Row(
        controls=[left_panel, right_panel],
        expand=True,
        spacing=0,
    )
    page.add(row_layer)



ft.app(main)
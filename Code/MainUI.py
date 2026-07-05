import flet as ft

def main(page: ft.Page):
    page.title="BAMessage"
    page.padding=0


    fake_users = ["星野", "李四", "王五"]

    user_tiles = []
    for name in fake_users:
        # 这里假设你的图片文件名和用户名对应，比如 "张三.png"
        avatar = ft.CircleAvatar(
            foreground_image_src=f"Image/{name}.png",
            radius=20,  # 设置小一点，适合列表
        )
        user_tiles.append(
            ft.ListTile(
                leading=avatar,
                title=ft.Text(name),
            )
        )
    # ListView 用 expand=True 撑满父容器的高度
    left_list = ft.ListView(
        controls=user_tiles,
        spacing=0,
        padding=10,
        expand=True,  # 高度自动填满 left_panel
        width=175
    )

    left_panel = ft.Container(
        content=left_list,
        bgcolor=ft.Colors.WHITE_12,
        alignment=ft.Alignment.CENTER, # 让文字居中
    )

# 2. 右边：就是一个白色方块，里面写个“右”
    right_panel = ft.Container(
        content=ft.Text("右边聊天区", size=20),
        bgcolor=ft.Colors.WHITE,
        alignment=ft.Alignment.CENTER,
        expand=True,
    )
    row_layer=ft.Row(
        controls=[left_panel, right_panel],
        expand=True,
        spacing=0,
    )
    page.add(row_layer)



ft.app(main)
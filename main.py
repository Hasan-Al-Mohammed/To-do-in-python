import flet as ft

def main(page: ft.Page):
    page.title = "Tools"
    page.bgcolor = "#1E1E2C"  # لون الخلفية الداكن
    page.padding = 20

    # تنسيق النصوص
    title_style = ft.TextStyle(size=18, weight=ft.FontWeight.BOLD, color="#FF4C4C")

    # محول الوحدات
    unit_input = ft.TextField(label="أدخل القيمة", text_align=ft.TextAlign.RIGHT)
    unit_from = ft.Dropdown(options=[ft.dropdown.Option("كيلومتر"), ft.dropdown.Option("متر")])
    unit_to = ft.Dropdown(options=[ft.dropdown.Option("كيلومتر"), ft.dropdown.Option("متر")])
    convert_button = ft.ElevatedButton("تحويل", bgcolor="#FF4C4C", color="white")

    unit_converter = ft.Column([
        ft.Text("محول الوحدات", style=title_style),
        ft.Row([unit_input, unit_from], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.Row([convert_button, unit_to], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    ])

    # الآلة الحاسبة
    num1 = ft.TextField(label="الرقم الأول", text_align=ft.TextAlign.RIGHT)
    num2 = ft.TextField(label="الرقم الثاني", text_align=ft.TextAlign.RIGHT)
    operator = ft.Dropdown(options=[ft.dropdown.Option("+"), ft.dropdown.Option("-"), ft.dropdown.Option("*"), ft.dropdown.Option("/")])
    calc_button = ft.ElevatedButton("احسب", bgcolor="#FF4C4C", color="white")

    calculator = ft.Column([
        ft.Text("آلة حاسبة", style=title_style),
        ft.Row([num1, num2, operator], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        calc_button
    ])

    # عداد تنازلي
    timer_input = ft.TextField(label="الوقت (بالثواني)", text_align=ft.TextAlign.RIGHT)
    timer_button = ft.ElevatedButton("ابدأ", bgcolor="#FF4C4C", color="white")

    countdown = ft.Column([
        ft.Text("عداد تنازلي", style=title_style),
        ft.Row([timer_input, timer_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    ])

    # قائمة المهام
    task_input = ft.TextField(label="أدخل مهمة جديدة", text_align=ft.TextAlign.RIGHT)
    task_button = ft.ElevatedButton("إضافة", bgcolor="#FF4C4C", color="white")

    task_list = ft.Column([])

    def add_task(e):
        if task_input.value:
            task_list.controls.append(ft.Text(task_input.value, color="white"))
            task_input.value = ""
            page.update()

    task_button.on_click = add_task

    tasks = ft.Column([
        ft.Text("قائمة مهام", style=title_style),
        ft.Row([task_input, task_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        task_list
    ])

    # إضافة جميع الأدوات إلى الصفحة
    page.add(unit_converter, calculator, countdown, tasks)

ft.app(target=main)

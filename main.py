import flet as ft
import json
import os

TASKS_FILE = "tasks.json"

# تحميل المهام المحفوظة
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# حفظ المهام إلى ملف
def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=4)

def main(page: ft.Page):
    page.title = "أدوات سريعة"
    page.bgcolor = "#1E1E2C"  # خلفية داكنة
    page.scroll = "adaptive"  # السماح بالتمرير في الأجهزة الصغيرة
    page.padding = 20

    title_style = ft.TextStyle(size=20, weight=ft.FontWeight.BOLD, color="#FF4C4C")

    # ===== محول الوحدات =====
    unit_input = ft.TextField(label="أدخل القيمة", text_align=ft.TextAlign.RIGHT)
    unit_from = ft.Dropdown(
        options=[
            ft.dropdown.Option("كيلومتر"),
            ft.dropdown.Option("متر"),
            ft.dropdown.Option("سنتيمتر"),
            ft.dropdown.Option("ميل"),
            ft.dropdown.Option("ياردة"),
        ]
    )
    unit_to = ft.Dropdown(
        options=[
            ft.dropdown.Option("كيلومتر"),
            ft.dropdown.Option("متر"),
            ft.dropdown.Option("سنتيمتر"),
            ft.dropdown.Option("ميل"),
            ft.dropdown.Option("ياردة"),
        ]
    )
    convert_result = ft.Text("", color="white")

    def convert_units(e):
        try:
            value = float(unit_input.value)
            conversions = {
                "كيلومتر": {"متر": 1000, "سنتيمتر": 100000, "ميل": 0.621371, "ياردة": 1093.61},
                "متر": {"كيلومتر": 0.001, "سنتيمتر": 100, "ميل": 0.000621371, "ياردة": 1.09361},
                "سنتيمتر": {"كيلومتر": 0.00001, "متر": 0.01, "ميل": 6.2137e-6, "ياردة": 0.0109361},
                "ميل": {"كيلومتر": 1.60934, "متر": 1609.34, "سنتيمتر": 160934, "ياردة": 1760},
                "ياردة": {"كيلومتر": 0.0009144, "متر": 0.9144, "سنتيمتر": 91.44, "ميل": 0.000568182},
            }
            result = value * conversions[unit_from.value][unit_to.value]
            convert_result.value = f"النتيجة: {result:.2f} {unit_to.value}"
        except:
            convert_result.value = "خطأ في الإدخال!"
        page.update()

    convert_button = ft.ElevatedButton("تحويل", bgcolor="#FF4C4C", color="white", on_click=convert_units)

    unit_converter = ft.Column([
        ft.Text("محول الوحدات", style=title_style),
        unit_input, unit_from, unit_to, convert_button, convert_result
    ], spacing=10)

    # ===== الآلة الحاسبة =====
    num1 = ft.TextField(label="الرقم الأول", text_align=ft.TextAlign.RIGHT)
    num2 = ft.TextField(label="الرقم الثاني", text_align=ft.TextAlign.RIGHT)
    operator = ft.Dropdown(options=[ft.dropdown.Option("+"), ft.dropdown.Option("-"), ft.dropdown.Option("*"), ft.dropdown.Option("/")])
    calc_result = ft.Text("", color="white")

    def calculate(e):
        try:
            a, b = float(num1.value), float(num2.value)
            if operator.value == "+": result = a + b
            elif operator.value == "-": result = a - b
            elif operator.value == "*": result = a * b
            elif operator.value == "/": result = a / b if b != 0 else "خطأ: قسمة على صفر!"
            calc_result.value = f"النتيجة: {result}"
        except:
            calc_result.value = "خطأ في الإدخال!"
        page.update()

    calc_button = ft.ElevatedButton("احسب", bgcolor="#FF4C4C", color="white", on_click=calculate)

    calculator = ft.Column([
        ft.Text("آلة حاسبة", style=title_style),
        num1, num2, operator, calc_button, calc_result
    ], spacing=10)

    # ===== العداد التنازلي =====
    timer_input = ft.TextField(label="الوقت (بالثواني)", text_align=ft.TextAlign.RIGHT)
    timer_text = ft.Text("", color="white")

    def start_timer(e):
        try:
            time_left = int(timer_input.value)
            timer_text.value = f"تبقى: {time_left} ثانية"
            page.update()
            while time_left > 0:
                time_left -= 1
                timer_text.value = f"تبقى: {time_left} ثانية"
                page.update()
                page.sleep(1)
            timer_text.value = "انتهى الوقت!"
        except:
            timer_text.value = "خطأ في الإدخال!"
        page.update()

    timer_button = ft.ElevatedButton("ابدأ", bgcolor="#FF4C4C", color="white", on_click=start_timer)

    countdown = ft.Column([
        ft.Text("عداد تنازلي", style=title_style),
        timer_input, timer_button, timer_text
    ], spacing=10)

    # ===== قائمة المهام =====
    tasks = load_tasks()
    task_input = ft.TextField(label="أدخل مهمة جديدة", text_align=ft.TextAlign.RIGHT)
    task_list = ft.Column([ft.Text(task, color="white") for task in tasks])

    def add_task(e):
        if task_input.value:
            tasks.append(task_input.value)
            task_list.controls.append(ft.Row([
                ft.Text(task_input.value, color="white"),
                ft.IconButton(ft.icons.DELETE, on_click=lambda e, t=task_input.value: remove_task(e, t))
            ]))
            task_input.value = ""
            save_tasks(tasks)
            page.update()

    def remove_task(e, task):
        tasks.remove(task)
        save_tasks(tasks)
        task_list.controls.clear()
        for t in tasks:
            task_list.controls.append(ft.Row([
                ft.Text(t, color="white"),
                ft.IconButton(ft.icons.DELETE, on_click=lambda e, t=t: remove_task(e, t))
            ]))
        page.update()

    task_button = ft.ElevatedButton("إضافة", bgcolor="#FF4C4C", color="white", on_click=add_task)

    task_manager = ft.Column([
        ft.Text("قائمة مهام", style=title_style),
        task_input, task_button, task_list
    ], spacing=10)

    # إضافة جميع الأدوات إلى الصفحة
    page.add(unit_converter, calculator, countdown, task_manager)

ft.app(target=main)

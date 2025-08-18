import math
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

#settings and constants
methods = ["Через основание и высоту", "Через две стороны и угол"]
program_name = "Расчет площади треугольника"
error_message = "Ошибка: Пожалуйста, введите числовые значения."
radians = "Радианы"
degrees = "Градусы"
calc_btn_text = "Рассчитать площадь"
answer_title = "Ответ"

padding = 25




def clear_old_widgets():
    for widget in frame.winfo_children():
        if widget not in global_widgets:
            widget.destroy()

def selected(event):
    if combobox.get() == methods[0]:
        with_base_height()
    elif combobox.get() == methods[1]:
        with_two_sides()

def with_base_height():
    clear_old_widgets()
    base_label = tk.Label(master=frame, text="основание треугольника:")
    base_label.grid(row=2, column=1)
    base_entry = tk.Entry(master=frame)
    base_entry.grid(row=2, column=2)

    height_label = tk.Label(master=frame, text="высота треугольника:")
    height_label.grid(row=3, column=1)
    height_entry = tk.Entry(master=frame)
    height_entry.grid(row=3, column=2)

    calc_base_height_button = tk.Button(
        master=frame,
        text=calc_btn_text,
        command=lambda: messagebox.showinfo(answer_title, calculate_base_height_area(base_entry.get(), height_entry.get())))
    calc_base_height_button.grid(row=4, column=2)

def calculate_base_height_area(base, height):
    try:
        base_float = float(base)
        height_float = float(height)

        return "Площадь равна: " + str(round(base_float * height_float / 2, 2))
    except ValueError:
        return error_message

def with_two_sides():
    clear_old_widgets()
    side_a_label = tk.Label(master=frame, text="Первая сторона треугольника:")
    side_a_label.grid(row=2, column=1)
    side_a_entry = tk.Entry(master=frame)
    side_a_entry.grid(row=2, column=2)

    side_b_label = tk.Label(master=frame, text="Вторая сторона треугольника:")
    side_b_label.grid(row=3, column=1)
    side_b_entry = tk.Entry(master=frame)
    side_b_entry.grid(row=3, column=2)

    angle_label = tk.Label(master=frame, text="Угол между сторонами:")
    angle_label.grid(row=4, column=1)
    angle_entry = tk.Entry(master=frame)
    angle_entry.grid(row=4, column=2)

    var = StringVar()
    var.set(degrees)
    deegres_radiobutton = tk.Radiobutton(frame, text=degrees, variable=var, value=degrees)
    radians_radiobutton = tk.Radiobutton(frame, text=radians, variable=var, value=radians)
    deegres_radiobutton.grid(row=5, column=1)
    radians_radiobutton.grid(row=5, column=2)


    calc_two_sides_button = tk.Button(
        master=frame,
        text=calc_btn_text,
        command=lambda: messagebox.showinfo(answer_title, calculate_two_sides_area(side_a_entry.get(), side_b_entry.get(), angle_entry.get(), var.get())))
    calc_two_sides_button.grid(row=6, column=2)

def calculate_two_sides_area(side_a, side_b, angle, variant):
    try:
        side_a_float = float(side_a)
        side_b_float = float(side_b)
        angle_float = float(angle)
        if variant == degrees:
            angle_float = angle_float * round(math.pi, 2) / 180
        return "Площадь равна: " + str(round(side_a_float * side_b_float * math.sin(angle_float) / 2, 2))
    except ValueError:
        return error_message


if __name__ == '__main__':
    main_window = tk.Tk()

    frame = tk.Frame(master=main_window,padx=padding, pady=padding)
    frame.pack(expand=True, fill="both")

    method_label = tk.Label(master=frame, text="Метод расчета площади треугольника:")
    method_label.grid(row=1, column=1)

    combobox = ttk.Combobox(master=frame, values=methods, state="readonly", width=30)
    combobox.grid(row=1, column=2)
    combobox.set(value = "Выберите метод")
    combobox.bind("<<ComboboxSelected>>", selected)

    global_widgets = frame.winfo_children()

    main_window.title(program_name)
    main_window.geometry("500x200")
    main_window.mainloop()


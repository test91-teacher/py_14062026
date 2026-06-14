import tkinter as tk

window = tk.Tk()
window.title("Мои задачи: Перенос элементов")
window.geometry("800x600") # Увеличили ширину, чтобы всё точно влезло

# --- Настройки стилей для списков ---
listbox_style = {
    "bg": "lightblue",
    "fg": "black",
    "font": ("Arial", 12),
    "width": 25,
    "height": 12,
    "selectmode": tk.SINGLE
}

# ==========================================
# ЛЕВАЯ ЧАСТЬ: Первый Listbox
# ==========================================
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# ВАЖНО: Сначала пакуем скроллбар!
scrollbar1 = tk.Scrollbar(left_frame)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)

# Потом пакуем список
lb1 = tk.Listbox(left_frame, **listbox_style)
lb1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

lb1.config(yscrollcommand=scrollbar1.set)
scrollbar1.config(command=lb1.yview)

for i in range(50):
    lb1.insert(tk.END, f"Элемент {i+1}")


# ==========================================
# СРЕДНЯЯ ЧАСТЬ: Кнопки управления
# ==========================================
mid_frame = tk.Frame(window)
mid_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=10)

def move_to_right():
    selected = lb1.curselection()
    if selected:
        item_text = lb1.get(selected[0])
        lb1.delete(selected[0])
        lb2.insert(tk.END, item_text)

def move_to_left():
    selected = lb2.curselection()
    if selected:
        item_text = lb2.get(selected[0])
        lb2.delete(selected[0])
        lb1.insert(tk.END, item_text)

# Сделал кнопки компактнее (просто стрелки), чтобы сэкономить место по ширине
btn_right = tk.Button(mid_frame, text="➔", command=move_to_right, width=3, font=("Arial", 16))
btn_right.pack(pady=20)

btn_left = tk.Button(mid_frame, text="⬅", command=move_to_left, width=3, font=("Arial", 16))
btn_left.pack(pady=20)


# ==========================================
# ПРАВАЯ ЧАСТЬ: Второй Listbox
# ==========================================
right_frame = tk.Frame(window)
right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# ВАЖНО: Снова сначала пакуем скроллбар!
scrollbar2 = tk.Scrollbar(right_frame)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

# Потом пакуем список
lb2 = tk.Listbox(right_frame, **listbox_style)
lb2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

lb2.config(yscrollcommand=scrollbar2.set)
scrollbar2.config(command=lb2.yview)


window.mainloop()
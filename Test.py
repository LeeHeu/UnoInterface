import tkinter as tk
from tkinter import ttk

def on_value_change(event):
    # Lấy giá trị hiện tại của slider
    value = slider.get()
    # Cập nhật nhãn với giá trị mới
    label.config(text=f"Giá trị hiện tại: {value}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Slider Example")

# Tạo một thanh trượt
slider = ttk.Scale(root, from_=0, to=100, orient='horizontal', command=on_value_change)
slider.pack(fill='x', padx=10, pady=10)

# Tạo một nhãn để hiển thị giá trị
label = ttk.Label(root, text="Kéo thanh trượt")
label.pack(pady=10)

# Bắt đầu vòng lặp chính của giao diện
root.mainloop()

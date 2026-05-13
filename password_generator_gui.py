import random
import string
import tkinter as tk
from tkinter import ttk, messagebox

LOWER = string.ascii_lowercase
UPPER = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

class PasswordGeneratorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🔐 Генератор Паролей")
        self.root.geometry("640x560")
        self.root.resizable(False, False)
        self.root.configure(bg="#0a0a0a")
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="ГЕНЕРАТОР ПАРОЛЕЙ", font=("Segoe UI", 22, "bold"), 
                fg="#00ff9d", bg="#0a0a0a").pack(pady=25)
        
        # Длина
        frame = tk.Frame(self.root, bg="#0a0a0a")
        frame.pack(pady=10)
        tk.Label(frame, text="Длина пароля:", font=("Segoe UI", 11), bg="#0a0a0a", fg="white").pack(side=tk.LEFT, padx=10)
        self.length_var = tk.IntVar(value=16)
        tk.Spinbox(frame, from_=6, to=50, width=6, textvariable=self.length_var, font=("Consolas", 12), bg="#1f1f1f", fg="#00ff9d").pack(side=tk.LEFT)
        
        # Чекбоксы
        types = tk.LabelFrame(self.root, text=" Типы символов ", fg="#00ff9d", bg="#0a0a0a", font=("Segoe UI", 10, "bold"))
        types.pack(pady=20, padx=50, fill="x")
        
        self.v_lower = tk.BooleanVar(value=True)
        self.v_upper = tk.BooleanVar(value=True)
        self.v_digit = tk.BooleanVar(value=True)
        self.v_spec = tk.BooleanVar(value=True)
        
        tk.Checkbutton(types, text="a-z строчные", variable=self.v_lower, bg="#0a0a0a", fg="white", selectcolor="#1f1f1f").grid(row=0, column=0, pady=6, padx=30, sticky="w")
        tk.Checkbutton(types, text="A-Z заглавные", variable=self.v_upper, bg="#0a0a0a", fg="white", selectcolor="#1f1f1f").grid(row=0, column=1, pady=6, padx=30, sticky="w")
        tk.Checkbutton(types, text="0-9 цифры", variable=self.v_digit, bg="#0a0a0a", fg="white", selectcolor="#1f1f1f").grid(row=1, column=0, pady=6, padx=30, sticky="w")
        tk.Checkbutton(types, text="!@#$ спецсимволы", variable=self.v_spec, bg="#0a0a0a", fg="white", selectcolor="#1f1f1f").grid(row=1, column=1, pady=6, padx=30, sticky="w")
        
        # Кнопки генерации
        btn_frame = tk.Frame(self.root, bg="#0a0a0a")
        btn_frame.pack(pady=20)
        
        tk.Button(btn_frame, text="ПРОСТОЙ", width=12, height=2, bg="#1f1f1f", fg="#00ff9d", command=self.simple).grid(row=0, column=0, padx=8)
        tk.Button(btn_frame, text="СЛОЖНЫЙ", width=12, height=2, bg="#1f1f1f", fg="#00ff9d", command=self.complex).grid(row=0, column=1, padx=8)
        tk.Button(btn_frame, text="С НАСТРОЙКАМИ", width=16, height=2, bg="#00ff9d", fg="black", command=self.custom).grid(row=0, column=2, padx=8)
        
        # Поле пароля
        tk.Label(self.root, text="Ваш пароль:", bg="#0a0a0a", fg="#00ff9d", font=("Segoe UI", 11)).pack(pady=(10,5))
        self.pass_entry = tk.Entry(self.root, font=("Consolas", 16, "bold"), width=40, justify="center", bg="#1f1f1f", fg="#00ff9d", readonlybackground="#1f1f1f")
        self.pass_entry.pack(pady=8)
        
        tk.Button(self.root, text="📋 КОПИРОВАТЬ В БУФЕР", bg="#00ff9d", fg="black", height=2, command=self.copy).pack(pady=15)
    
    def generate(self):
        chars = ""
        if self.v_lower.get(): chars += LOWER
        if self.v_upper.get(): chars += UPPER
        if self.v_digit.get(): chars += DIGITS
        if self.v_spec.get(): chars += SPECIAL
        
        if not chars:
            messagebox.showerror("Ошибка", "Выберите хотя бы один тип символов!")
            return None
        
        length = self.length_var.get()
        pwd = ''.join(random.choice(chars) for _ in range(length))
        pwd_list = list(pwd)
        random.shuffle(pwd_list)
        return ''.join(pwd_list)
    
    def show(self, password):
        self.pass_entry.delete(0, tk.END)
        self.pass_entry.insert(0, password)
        messagebox.showinfo("✅ Успешно!", f"Пароль сгенерирован!\n\n{password}")
    
    def simple(self): 
        self.v_lower.set(True); self.v_upper.set(False); self.v_digit.set(True); self.v_spec.set(False)
        pwd = self.generate()
        if pwd: self.show(pwd)
    
    def complex(self):
        self.v_lower.set(True); self.v_upper.set(True); self.v_digit.set(True); self.v_spec.set(True)
        pwd = self.generate()
        if pwd: self.show(pwd)
    
    def custom(self):
        pwd = self.generate()
        if pwd: self.show(pwd)
    
    def copy(self):
        pwd = self.pass_entry.get()
        if pwd:
            self.root.clipboard_clear()
            self.root.clipboard_append(pwd)
            messagebox.showinfo("📋 Скопировано", "Пароль скопирован в буфер обмена!")

if __name__ == "__main__":
    app = PasswordGeneratorGUI()
    app.root.mainloop()
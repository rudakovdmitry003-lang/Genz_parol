import customtkinter as ctk
import threading
import time
from pynput.mouse import Button, Controller

ctk.set_appearance_mode("dark")        # Темная тема
ctk.set_default_color_theme("blue")    # Синяя тема

class AutoClicker(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🌟 Ultra Clicker")
        self.geometry("420x520")
        self.resizable(False, False)

        self.running = False
        self.mouse = Controller()
        self.click_thread = None

        # Переменные
        self.cps = ctk.IntVar(value=50)
        self.button_var = ctk.StringVar(value="Левая кнопка")

        self.create_widgets()

    def create_widgets(self):
        # Заголовок
        title = ctk.CTkLabel(self, text="🌟 ULTRA CLICKER", 
                           font=ctk.CTkFont(size=28, weight="bold"))
        title.pack(pady=20)

        # Статус
        self.status_label = ctk.CTkLabel(self, text="● Остановлен", 
                                       text_color="red",
                                       font=ctk.CTkFont(size=16))
        self.status_label.pack(pady=5)

        # CPS
        ctk.CTkLabel(self, text="Скорость кликов (CPS)", 
                    font=ctk.CTkFont(size=16)).pack(pady=(20,5))
        
        self.cps_slider = ctk.CTkSlider(self, from_=1, to=500, 
                                      number_of_steps=499,
                                      variable=self.cps,
                                      width=300)
        self.cps_slider.pack(pady=5)
        
        self.cps_value = ctk.CTkLabel(self, text="50 CPS", 
                                    font=ctk.CTkFont(size=18, weight="bold"))
        self.cps_value.pack(pady=5)

        # Обновление значения CPS
        self.cps_slider.configure(command=self.update_cps_label)

        # Кнопка мыши
        ctk.CTkLabel(self, text="Кнопка мыши", 
                    font=ctk.CTkFont(size=16)).pack(pady=(20,5))
        
        self.button_menu = ctk.CTkOptionMenu(self,
                                           values=["Левая кнопка", "Правая кнопка"],
                                           variable=self.button_var,
                                           width=200)
        self.button_menu.pack(pady=10)

        # Основная кнопка
        self.toggle_button = ctk.CTkButton(self, text="▶ ЗАПУСТИТЬ КЛИКЕР",
                                         font=ctk.CTkFont(size=18, weight="bold"),
                                         height=60,
                                         fg_color="#00ff88",
                                         text_color="black",
                                         hover_color="#00cc6a",
                                         command=self.toggle_clicker)
        self.toggle_button.pack(pady=30, padx=40, fill="x")

        # Горячие клавиши
        info = ctk.CTkLabel(self, text="Горячие клавиши:\n"
                                      "F6 — Запуск / Остановка\n"
                                      "ESC — Выход из программы",
                           font=ctk.CTkFont(size=12),
                           text_color="gray")
        info.pack(pady=10)

        # Нижняя информация
        footer = ctk.CTkLabel(self, text="Made with ❤️ for you", 
                            text_color="gray", font=ctk.CTkFont(size=10))
        footer.pack(side="bottom", pady=15)

    def update_cps_label(self, value):
        cps = int(value)
        self.cps_value.configure(text=f"{cps} CPS")

    def clicker_loop(self):
        delay = 1.0 / self.cps.get()
        button = Button.left if self.button_var.get() == "Левая кнопка" else Button.right

        while self.running:
            self.mouse.click(button)
            time.sleep(delay)

    def toggle_clicker(self):
        if not self.running:
            # Запуск
            self.running = True
            self.status_label.configure(text="● Работает", text_color="lime")
            self.toggle_button.configure(text="⏹ ОСТАНОВИТЬ", fg_color="#ff4444")
            
            self.click_thread = threading.Thread(target=self.clicker_loop, daemon=True)
            self.click_thread.start()
        else:
            # Остановка
            self.running = False
            self.status_label.configure(text="● Остановлен", text_color="red")
            self.toggle_button.configure(text="▶ ЗАПУСТИТЬ КЛИКЕР", fg_color="#00ff88")

    def start_hotkeys(self):
        """Горячие клавиши"""
        from pynput import keyboard

        def on_press(key):
            try:
                if key == keyboard.Key.f6:
                    self.after(0, self.toggle_clicker)
                elif key == keyboard.Key.esc:
                    self.after(0, self.destroy)
            except:
                pass

        listener = keyboard.Listener(on_press=on_press)
        listener.start()


if __name__ == "__main__":
    app = AutoClicker()
    app.start_hotkeys()
    app.mainloop()
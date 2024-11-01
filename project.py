import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("เครื่องคิดเลข")
        self.window.geometry("300x400")

        # หน้าจอแสดงผล
        self.display = tk.Entry(self.window, width=30, justify="right", font=('Arial', 14))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # ปุ่มตัวเลขและเครื่องหมาย
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # สร้างปุ่ม
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(self.window, text=button, command=cmd, width=10).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # ปุ่มล้างข้อมูล
        ttk.Button(self.window, text='C', command=self.clear, width=10).grid(row=row, column=col, padx=2, pady=2)

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)

    def clear(self):
        self.display.delete(0, tk.END)

    def run(self):
        self.window.mainloop()

# สร้างและรันแอพพลิเคชั่น
if __name__ == '__main__':
    calc = Calculator()
    calc.run()

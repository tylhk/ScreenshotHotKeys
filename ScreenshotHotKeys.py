import tkinter as tk
from tkinter import messagebox
import os

class KeyDetectorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("修改截图快捷键")
        
        # 地址输入框
        self.address_label = tk.Label(root, text="文件保存路径(请按照说明填写)：")
        self.address_label.pack(pady=5)
        self.address_entry = tk.Entry(root, width=40)
        self.address_entry.pack(pady=5)
        
        # 按键检测按钮
        self.detect_button = tk.Button(root, text="检测组合键", command=self.show_key_detection)
        self.detect_button.pack(pady=10)
        
        # 按键显示标签
        self.key_label = tk.Label(root, text="当前组合键：无")
        self.key_label.pack(pady=5)
        
        # 文件生成按钮
        self.generate_button = tk.Button(root, text="生成AHK文件", command=self.generate_ahk_file)
        self.generate_button.pack(pady=10)
        
        # 组合键存储变量
        self.key_combination = ""

    def show_key_detection(self):
        """弹出组合键检测窗口"""
        popup = tk.Toplevel(self.root)
        popup.title("按住组合键")
        popup.geometry("300x100")
        
        info_label = tk.Label(popup, text="请按住组合键后关闭此窗口")
        info_label.pack(pady=10)
        
        pressed_keys = set()
        
        def update_keys(event, is_press):
            """处理按键事件"""
            key = event.keysym
            # 统一修饰键名称
            if key.startswith(('Alt', 'Control', 'Shift')):
                key = key.split('_')[0]
            if is_press:
                pressed_keys.add(key)
            else:
                if key in pressed_keys:
                    pressed_keys.remove(key)
            # 实时显示
            current_keys = "+".join(sorted(pressed_keys, key=str.lower))
            info_label.config(text=f"当前按键：{current_keys}")
        
        popup.bind("<KeyPress>", lambda e: update_keys(e, True))  # [[1, 8, 10]]
        popup.bind("<KeyRelease>", lambda e: update_keys(e, False))
        
        def save_keys():
            """保存组合键并关闭窗口"""
            self.key_combination = "+".join(sorted(pressed_keys, key=str.lower))
            self.key_label.config(text=f"当前组合键：{self.key_combination}")
            popup.destroy()
        
        popup.protocol("WM_DELETE_WINDOW", save_keys)
        popup.grab_set()  # 模态窗口 [[19]]

    def generate_ahk_file(self):
        """生成AHK文件"""
        path = self.address_entry.get()
        if not path:
            messagebox.showerror("错误", "请输入保存路径！")
            return
        if not self.key_combination:
            messagebox.showerror("错误", "请先检测组合键！")
            return
        
        try:
            def move_char_to_front(s, target_char):
                index = s.find(target_char)
                if index == -1:
                    return s
                return target_char + s[:index] + s[index+1:]
            self.key_combination_copy=self.key_combination
            self.key_combination_copy=self.key_combination_copy.replace("+","")
            self.key_combination_copy=self.key_combination_copy.replace("Alt","!")
            self.key_combination_copy=self.key_combination_copy.replace("Control","^")
            self.key_combination_copy=self.key_combination_copy.replace("Shift","+")
            self.key_combination_copy=self.key_combination_copy.replace("Win_L","#")
            self.key_combination_copy=move_char_to_front(self.key_combination_copy, '+')
            self.key_combination_copy=move_char_to_front(self.key_combination_copy, '!')
            self.key_combination_copy=move_char_to_front(self.key_combination_copy, '#')
            self.key_combination_copy=move_char_to_front(self.key_combination_copy, '^')
            os.makedirs(path, exist_ok=True)
            file_path = os.path.join(path, "test.ahk")
            with open(file_path, 'w') as f:
                f.write(f"{self.key_combination_copy}::#+S\n")
            messagebox.showinfo("成功", f"文件已生成：\n{file_path}")
        except Exception as e:
            messagebox.showerror("错误", f"文件生成失败：\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = KeyDetectorApp(root)
    root.mainloop()

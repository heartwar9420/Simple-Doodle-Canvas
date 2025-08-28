# 塗鴉_使用_canvas
import tkinter as tk
from tkinter import colorchooser
class 畫畫類別():
    def __init__(self, 視窗物件):
        self.app = 視窗物件
        self.app.title("簡易塗鴉畫板")
        self.app.geometry("800x600")
        self.app.config(bg='gray80')

        # 蘇有物件的繪圖屬性
        self.drawing = False
        self.last_x = None
        self.last_y = None
        self.brush_size = 5
        self.brush_color = "black"
        self.eraser_mode = False

        # 創建工具列
        self.create_toolbar()

        # 創建畫布
        self.canvas = tk.Canvas(self.app, bg="gray90",
                                width=700, height=500, cursor="dot")
        self.canvas.pack(expand=True)

        # 綁定滑鼠事件
        self.canvas.bind("<Button-1>", self.start_drawing)  # 滑鼠左鍵按下
        self.canvas.bind("<B1-Motion>", self.draw)          # 滑鼠移動
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)  # 滑鼠左鍵放開
    def create_toolbar(self):
        """創建簡單的工具列"""
        toolbar = tk.Frame(self.app,bg='gray80')
        toolbar.pack(side=tk.TOP,anchor=tk.W)

        # 顏色選擇按鈕
        colors = ["black", "red", "green", "blue", "yellow", "purple", "orange"]
        for color in colors:
            btn = tk.Button(toolbar, bg=color,
                            width=3,
                            #height=1,
                            command = lambda c = color : self.set_color(c) )
            btn.pack(side=tk.LEFT,padx=10,pady=10)

        # 自訂顏色按鈕
        custom_btn = tk.Button(toolbar, text="更多顏色", command=self.choose_custom_color)
        custom_btn.pack(side=tk.LEFT,padx=10,pady=10)

        # 畫筆/橡皮擦切換
        self.eraser_btn = tk.Button(toolbar, text="畫筆", command=self.toggle_eraser)
        self.eraser_btn.pack(side=tk.LEFT,padx=10,pady=10)

        # 畫筆大小調整
        size_label = tk.Label(toolbar, text="大小:",font=("Helvetica", 14),bg='gray80')
        size_label.pack(side=tk.LEFT,padx=1,pady=10)

        self.size_scale = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL, # Scale 數值調整滑桿
                                   length=100, command=self.update_brush_size)
        self.size_scale.set(self.brush_size)
        self.size_scale.pack(side=tk.LEFT,padx=1,pady=10)

        # 清除按鈕
        clear_btn = tk.Button(toolbar, text="清除畫布", command=self.clear_canvas)
        clear_btn.pack(side=tk.LEFT,padx=10,pady=10)
    def set_color(self, color):
        """設置畫筆顏色"""
        self.brush_color = color
        self.eraser_mode = False
        self.eraser_btn.config(text="畫筆")
    def choose_custom_color(self):
        """選擇自訂顏色"""
        color = colorchooser.askcolor(title="選擇顏色", initialcolor=self.brush_color)
        # print(color) # ((64, 128, 128), '#408080')
        if color[1]:
            self.set_color(color[1])
    def update_brush_size(self, value):
        """更新畫筆大小"""
        self.brush_size = int(value)
    def toggle_eraser(self):
        """切換橡皮擦模式"""
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.eraser_btn.config(text="橡皮擦")
        else:
            self.eraser_btn.config(text="畫筆")
    def start_drawing(self, event):
        """開始繪圖"""
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y
    def draw(self, event):
        """繪圖過程"""
        if self.drawing and self.last_x is not None and self.last_y is not None:
            if self.eraser_mode:
                # 橡皮擦模式 - 用白色畫筆覆蓋
                self.canvas.create_line(
                    self.last_x, self.last_y, event.x, event.y,
                    fill="gray90", width=self.brush_size * 2,
                    capstyle=tk.ROUND, smooth=True
                )
            else:
                # 畫筆模式
                self.canvas.create_line(
                    self.last_x, self.last_y, event.x, event.y,
                    fill=self.brush_color, width=self.brush_size,
                    capstyle=tk.ROUND, smooth=True
                )

            self.last_x = event.x
            self.last_y = event.y
    def stop_drawing(self, event):
        """停止繪圖"""
        self.drawing = False
        self.last_x = None
        self.last_y = None
    def clear_canvas(self):
        """清除畫布"""
        self.canvas.delete("all")
# 啟動應用程式
root = tk.Tk()
畫畫類別(root)
root.mainloop()

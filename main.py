import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import os
import tkextrafont
import tkinter.font as tkfont
from ui.frame1_home import create_frame1
from ui.frame2_blocker import create_frame2
from utils.helpers import resource_path

# ---------- Window Setup ----------
window = ctk.CTk()
window.title("Malicious Website Blocker")
window.geometry("400x500")
window.config(bg="#222222")

# ---------- Header ----------
frame = tk.Frame(window, bg="#222222")
frame.pack(pady=15, anchor="nw", side=tk.TOP, padx=30)

# Load header image
img_path = resource_path("assets/image.png")
img = Image.open(img_path).resize((140, 16), Image.Resampling.LANCZOS)
img_tk = ImageTk.PhotoImage(img)
img_label = tk.Label(frame, image=img_tk, bg="#222222")
img_label.image = img_tk
img_label.pack(side=tk.LEFT)

hr = tk.Frame(window, bg="#FF043C", height=2)
hr.pack(fill=tk.X, padx=30)

# ---------- Fonts ----------
splinesans = tkextrafont.Font(file=resource_path("assets/splinesans.ttf"), family="Spline Sans Mono")
squada = tkextrafont.Font(file=resource_path("assets/squada.ttf"), family="Squada One")

# Tkinter + CTk fonts
tk_spline_normal2 = tkfont.Font(family="Spline Sans Mono", size=10)
tk_squada_normal = tkfont.Font(family="Squada One", size=55)
ctk_spline_normal = ctk.CTkFont(family="Spline Sans Mono", size=12)
ctk_spline_bold = ctk.CTkFont(family="Spline Sans Mono", size=12, weight="bold")

# ---------- Frames ----------
body_frame = create_frame1(window, ctk_spline_bold, tk_spline_normal2, tk_squada_normal)
body2_frame = create_frame2(window, ctk_spline_bold, ctk_spline_normal)

# Navigation handlers
def go_to_frame2():
    body_frame.pack_forget()
    body2_frame.pack(fill="both", expand=True, pady=15)

def go_back_to_frame1():
    body2_frame.pack_forget()
    body_frame.pack(fill="both", expand=True, pady=20)

# Pass navigation callbacks
body_frame.go_to_frame2 = go_to_frame2
body2_frame.go_back_to_frame1 = go_back_to_frame1

body_frame.pack(fill="both", expand=True, padx=0, pady=20)

window.resizable(False, False)
window.mainloop()


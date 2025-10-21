import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from utils.email_utils import send_email
from utils.helpers import open_file

class Frame1(tk.Frame):
    def __init__(self, master, ctk_font_bold, tk_font_normal2, tk_font_title, *args, **kwargs):
        super().__init__(master, bg="#222222", *args, **kwargs)
        self.go_to_frame2 = None

        # Heading
        tk.Label(self, text="Welcome!", bg="#222222", fg="white", font=tk_font_title).grid(row=0, column=0, pady=(15, 0), padx=30, sticky="w")
        tk.Label(self, text="This tool helps you block malicious websites and check their safety using VirusTotal API.",
                 bg="#222222", fg="#7b7b7b", font=tk_font_normal2, wraplength=340, justify="left").grid(row=1, column=0, pady=10, sticky="w", padx=30)

        input_frame = tk.Frame(self, bg="#222222")
        input_frame.grid(row=3, column=0, padx=30, sticky="ew", pady=(0, 20))
        input_frame.grid_columnconfigure(1, weight=1)

        tk.Label(input_frame, text="Email:", bg="#222222", fg="white", font=("Spline Sans Mono", 12)).grid(row=2, column=0, sticky="w", pady=(20, 5))
        self.entry_email = ctk.CTkEntry(input_frame, font=("Spline Sans Mono", 12), border_width=0, corner_radius=10, placeholder_text="Enter your email")
        self.entry_email.grid(row=2, column=1, sticky="ew", pady=(20, 5), padx=(10, 0))

        ctk.CTkButton(self, command=self._send_email, text="Send Password", font=ctk_font_bold, fg_color="#FF043C", hover_color="#c8052f").grid(row=4, column=0, pady=(20,0), padx=30, sticky="ew")
        ctk.CTkButton(self, command=open_file, text="Project Info", font=ctk_font_bold, fg_color="#FF043C", hover_color="#c8052f").grid(row=5, column=0, pady=(20,0), padx=30, sticky="ew")
        ctk.CTkButton(self, command=lambda: self.go_to_frame2(), text="Next ->", font=ctk_font_bold,
                      fg_color="#222222", border_color="#FF043C", border_width=1, text_color="#FF043C", hover_color="#ffffff").grid(row=6, column=0, pady=(20,0), padx=30, sticky="ew")

    def _send_email(self):
        email = self.entry_email.get().strip()
        if not email:
            messagebox.showerror("Error", "Please enter your email address.")
            return
        send_email(email)

def create_frame1(window, ctk_font_bold, tk_font_normal2, tk_font_title):
    return Frame1(window, ctk_font_bold, tk_font_normal2, tk_font_title)


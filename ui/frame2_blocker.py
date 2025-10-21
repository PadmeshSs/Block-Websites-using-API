import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from utils.virustotal import checksite
from utils.hosts_manager import block_website, unblock_website, open_hosts_file
from utils.helpers import show_url_popup

class Frame2(tk.Frame):
    def __init__(self, master, ctk_font_bold, ctk_font_normal, *args, **kwargs):
        super().__init__(master, bg="#222222", *args, **kwargs)
        self.go_back_to_frame1 = None

        ctk.CTkButton(self, command=show_url_popup, text="URLs for Testing", font=ctk_font_bold,
                      fg_color="#FF043C", hover_color="#c8052f").grid(row=0, column=0, pady=(20,0), padx=30, sticky="ew")

        # Inputs
        input_frame = tk.Frame(self, bg="#222222")
        input_frame.grid(row=1, column=0, padx=30, sticky="ew", pady=(40,10))
        input_frame.grid_columnconfigure(1, weight=1)

        tk.Label(input_frame, text="URL:", bg="#222222", fg="white", font=("Spline Sans Mono", 12)).grid(row=1, column=0, sticky="w", pady=(20, 5))
        self.entry_url = ctk.CTkEntry(input_frame, font=ctk_font_normal, border_width=0, corner_radius=10, placeholder_text="Enter the URL")
        self.entry_url.grid(row=1, column=1, sticky="ew", pady=(20,5), padx=(10,0))

        tk.Label(input_frame, text="Password:", bg="#222222", fg="white", font=("Spline Sans Mono", 12)).grid(row=2, column=0, sticky="w", pady=(15, 5))
        self.entry_pass = ctk.CTkEntry(input_frame, font=ctk_font_normal, border_width=0, corner_radius=10, placeholder_text="Enter the Password", show="*")
        self.entry_pass.grid(row=2, column=1, sticky="ew", pady=(15, 5), padx=(10, 0))

        ctk.CTkButton(self, command=lambda: checksite(self.entry_url.get()), text="Check Website",
                      font=ctk_font_bold, fg_color="#FF043C", hover_color="#c8052f").grid(row=2, column=0, pady=(10,0))

        # Block/Unblock Buttons
        input_frame3 = tk.Frame(self, bg="#222222")
        input_frame3.grid(row=3, column=0, padx=30, sticky="ew", pady=10)
        input_frame3.grid_columnconfigure((0,1), weight=1)

        self.button_block = ctk.CTkButton(input_frame3, command=lambda: block_website(self.entry_url, self.entry_pass),
                                          text="Block", font=ctk_font_bold, fg_color="#FF043C", hover_color="#c8052f")
        self.button_block.grid(row=0, column=0, sticky="ew", padx=(0,5))
        
        ctk.CTkButton(input_frame3, command=lambda: unblock_website(self.entry_url, self.entry_pass),
                      text="Unblock", font=ctk_font_bold, fg_color="#FF043C", hover_color="#c8052f").grid(row=0, column=1, sticky="ew", padx=(5,0))

        ctk.CTkButton(self, command=open_hosts_file, text="Go to Host file", font=ctk_font_bold,
                      fg_color="#FF043C", hover_color="#c8052f").grid(row=4, column=0, pady=(40,0), padx=30, sticky="ew")

        ctk.CTkButton(self, command=lambda: self.go_back_to_frame1(), text="<- Back", font=ctk_font_bold,
                      fg_color="#222222", border_color="#FF043C", border_width=1, text_color="#FF043C", hover_color="#ffffff").grid(row=5, column=0, pady=(10,0), padx=30, sticky="ew")

def create_frame2(window, ctk_font_bold, ctk_font_normal):
    return Frame2(window, ctk_font_bold, ctk_font_normal)


import os
import sys
import webbrowser
import tkinter as tk
import customtkinter as ctk

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.dirname(base_path)
    return os.path.join(base_path, relative_path)

def open_file():
    file_path = resource_path("assets/info.pdf")
    if os.path.exists(file_path):
        webbrowser.open(f"file://{file_path}")
    else:
        print("File not found:", file_path)

def show_url_popup():
    popup = tk.Toplevel()
    popup.title("Available URLs")
    popup.geometry("400x300")
    popup.configure(bg="#222222")

    tk.Label(popup, text="Select and copy the URLs you want:",
             bg="#222222", fg="white", font=("Spline Sans Mono", 12)).pack(pady=10)
    
    urls = [
        "http://malicious-example1.com",
        "http://malicious-example2.com",
        "http://phishing-site.com",
        "http://dangerous-site.net",
        "http://suspicious-link.org"
    ]

    text_box = ctk.CTkTextbox(popup, font=("Spline Sans Mono", 12))
    text_box.pack(padx=20, pady=10, fill="both", expand=True)
    text_box.insert("end", "\n".join(urls))
    text_box.configure(state="normal")


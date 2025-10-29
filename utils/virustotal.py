import requests
from tkinter import messagebox
import os
from config import VIRUSTOTAL_API_KEY

def checksite(url):
    api_key = VIRUSTOTAL_API_KEY
    if not url:
        messagebox.showwarning("Warning", "Please enter a website URL")
        return

    params = {"apikey": api_key, "resource": url}

    try:
        response = requests.get("https://www.virustotal.com/vtapi/v2/url/report", params=params)
        result = response.json()

        if result.get("response_code") == 1:
            if result.get("positives", 0) > 0:
                messagebox.showwarning("Warning", "This website is malicious!")
            else:
                messagebox.showinfo("Info", "This website is safe")
        else:
            messagebox.showerror("Error", "Could not get scan result")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to check website: {e}")


import platform
import subprocess
from tkinter import messagebox
from utils.email_utils import password

def open_hosts_file():
    system_name = platform.system()
    if system_name == "Windows":
        subprocess.run(["powershell", "-Command", "Start-Process notepad.exe -ArgumentList 'C:\\Windows\\System32\\drivers\\etc\\hosts' -Verb RunAs"])
    elif system_name == "Linux":
        subprocess.run(["sudo", "xdg-open", "/etc/hosts"])
    elif system_name == "Darwin":
        subprocess.run(["sudo", "open", "-a", "TextEdit", "/etc/hosts"])
    else:
        messagebox.showerror("Error", f"Unsupported OS: {system_name}")

def get_hosts_path():
    system_name = platform.system()
    if system_name == "Windows":
        return r"C:\Windows\System32\drivers\etc\hosts"
    elif system_name in ("Linux", "Darwin"):
        return "/etc/hosts"
    return None

def block_website(entry_url, entry_pass):
    if entry_url.get() == "" or entry_pass.get() == "":
        messagebox.showerror("Error", "Enter both URL and Password")
        return
    if entry_pass.get() != password:
        messagebox.showerror("Error", "Invalid Password")
        return

    weburl = entry_url.get().strip().split("//")[-1]
    hosts_path = get_hosts_path()
    if not hosts_path: return

    entry = f"127.0.0.1 {weburl}\n127.0.0.1 www.{weburl}\n"
    try:
        with open(hosts_path, "a") as file:
            file.write(entry)
        messagebox.showinfo("Blocked", "Successfully Website Blocked")
        entry_pass.delete(0, "end")
    except PermissionError:
        messagebox.showerror("Error", "Run this script as Administrator/root!")

def unblock_website(entry_url, entry_pass):
    if entry_url.get() == "" or entry_pass.get() == "":
        messagebox.showerror("Error", "Enter both URL and Password")
        return
    if entry_pass.get() != password:
        messagebox.showerror("Error", "Invalid Password")
        return

    hosts_path = get_hosts_path()
    if not hosts_path: return

    try:
        with open(hosts_path, "r") as file:
            lines = file.readlines()
        with open(hosts_path, "w") as file:
            for line in lines:
                if entry_url.get() not in line:
                    file.write(line)
        messagebox.showinfo("Unblocked", "Successfully Website Unblocked")
        entry_pass.delete(0, "end")
    except PermissionError:
        messagebox.showerror("Error", "Run this script as Administrator/root!")


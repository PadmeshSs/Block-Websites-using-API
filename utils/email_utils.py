import re
import random
import string
import smtplib
from tkinter import messagebox
from email.mime.text import MIMEText
from config import SENDER_EMAIL, SENDER_PASSWORD

password = ''

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def send_email(recipient):
    global password
    password = generate_password()

    if not is_valid_email(recipient):
        messagebox.showerror("Error", "Invalid email format.")
        return

    sender_email = SENDER_EMAIL  
    sender_password = SENDER_PASSWORD

    msg = MIMEText(f"Hello,\n\nYour generated password:\n\n{password}\n\nKeep it safe!")
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = "Your Generated Password"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        messagebox.showinfo("Success", f"A password has been sent to {recipient}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email:\n{e}")


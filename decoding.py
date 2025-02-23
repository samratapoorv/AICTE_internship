import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def decode_message():
    file_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Failed to load image!")
        return

    password_input = simpledialog.askstring("Input", "Enter password:", show='*')
    key_file_path = file_path + ".key"

    if not os.path.exists(key_file_path):
        messagebox.showerror("Error", "Key file missing! Cannot verify password.")
        return
    
    with open(key_file_path, "r") as key_file:
        stored_password = key_file.read().strip()

    if password_input != stored_password:
        messagebox.showerror("Error", "Incorrect password!")
        return

    c = {i: chr(i) for i in range(255)}
    n, m, z = 0, 0, 0
    decoded_message = ""

    try:
        while n < img.shape[0] and m < img.shape[1]:
            decoded_message += c[img[n, m, z]]
            n, m = n + 1, m + 1
            z = (z + 1) % 3
    except KeyError:
        pass

    messagebox.showinfo("Decoded Message", f"Message: {decoded_message}")

root = tk.Tk()
root.withdraw()
decode_message()

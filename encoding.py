import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

def encode_message():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        return
    
    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Failed to load image!")
        return
    
    message = simpledialog.askstring("Input", "Enter the secret message:")
    password = simpledialog.askstring("Input", "Enter a password:", show='*')
    
    if not message or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return
    
    d = {chr(i): i for i in range(255)}
    n, m, z = 0, 0, 0

    for char in message:
        if n >= img.shape[0] or m >= img.shape[1]:
            messagebox.showerror("Error", "Message too long for this image!")
            return
        img[n, m, z] = d[char]
        n, m = n + 1, m + 1
        z = (z + 1) % 3

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        cv2.imwrite(save_path, img)
        with open(save_path + ".key", "w") as key_file:
            key_file.write(password)
        messagebox.showinfo("Success", "Message encoded successfully!")

root = tk.Tk()
root.withdraw()
encode_message()

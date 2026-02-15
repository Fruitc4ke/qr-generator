import qrcode
import tkinter as tk
from tkinter import messagebox

def generate_qr():
    url = entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    img = qrcode.make(url)
    img.save("generated_qr.png")
    messagebox.showinfo("Success", "QR Code saved as generated_qr.png")

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x150")

tk.Label(root, text="Enter URL:").pack(pady=5)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Generate QR", command=generate_qr).pack(pady=10)

root.mainloop()

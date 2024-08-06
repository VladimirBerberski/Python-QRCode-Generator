import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr_code(data, file_path, logo_path=None, box_size=10, border=4):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    if logo_path:
        logo = Image.open(logo_path)
        logo = logo.resize((box_size * 10, box_size * 10))
        img = img.convert("RGBA")
        logo = logo.convert("RGBA")
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos, mask=logo)

        

    img.save(file_path)
    return img

def select_logo():
    logo_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if logo_path:
        entry_logo_path.delete(0, tk.END)
        entry_logo_path.insert(0, logo_path)

def generate():
    data = entry_data.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if not data:
        messagebox.showerror("Error!", "Enter data for the QR code.")
        return
    if not file_path:
        return
    logo_path = entry_logo_path.get() if entry_logo_path.get() else None
    img = generate_qr_code(data, file_path, logo_path)
    img = ImageTk.PhotoImage(img)
    lbl_img.config(image=img)
    lbl_img.image = img
    messagebox.showinfo("Success", f"QR code is samed on {file_path}")

app = tk.Tk()
app.title("QR code generator")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

lbl_data = tk.Label(frame, text="Data:")
lbl_data.grid(row=0, column=0, sticky=tk.W, pady=5)

entry_data = tk.Entry(frame, width=50)
entry_data.grid(row=0, column=1, pady=5)

lbl_logo_path = tk.Label(frame, text="Logo:")
lbl_logo_path.grid(row=1, column=0, sticky=tk.W, pady=5)

entry_logo_path = tk.Entry(frame, width=50)
entry_logo_path.grid(row=1, column=1, pady=5)

btn_select_logo = tk.Button(frame, text="Files", command=select_logo)
btn_select_logo.grid(row=1, column=2, padx=5, pady=5)

btn_generate = tk.Button(frame, text="Generate QR code", command=generate)
btn_generate.grid(row=2, column=1, pady=10)

lbl_img = tk.Label(app)
lbl_img.pack(padx=10, pady=10)

app.mainloop()

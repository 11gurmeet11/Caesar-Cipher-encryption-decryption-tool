import tkinter as tk
from tkinter import ttk, messagebox

def caesar(text, shift):
    out = []
    for ch in text:
        if ch.isupper():
            out.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        elif ch.islower():
            out.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        else:
            out.append(ch)
    return "".join(out)

def action(enc=True):
    try:
        s = int(shift.get())
    except ValueError:
        return messagebox.showerror("Shift error", "Shift must be an integer")
    res.delete(0, tk.END)
    res.insert(0, caesar(txt.get(),  s if enc else -s))

root = tk.Tk()
root.title("🕶️ Caesar Cipher – Dark")
root.configure(bg="#1e1e1e")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", background="#1e1e1e", foreground="#e1e1e1")
style.configure("TEntry", fieldbackground="#2d2d2d", foreground="#e1e1e1")
style.configure("TButton", background="#3c3c3c", foreground="#ffffff")
style.map("TButton",
          background=[("active", "#5c5c5c")],
          foreground=[("disabled", "#888888")])

ttk.Label(root, text="Text").grid(row=0, column=0, padx=8, pady=8, sticky="e")
txt = ttk.Entry(root, width=40)
txt.grid(row=0, column=1, padx=8, pady=8)

ttk.Label(root, text="Shift").grid(row=1, column=0, sticky="e")
shift = ttk.Entry(root, width=6)
shift.grid(row=1, column=1, sticky="w", padx=8)

btn_frm = ttk.Frame(root)
btn_frm.grid(row=2, column=0, columnspan=2, pady=10)
ttk.Button(btn_frm, text="Encrypt", command=lambda: action(True)).pack(side="left", padx=5)
ttk.Button(btn_frm, text="Decrypt", command=lambda: action(False)).pack(side="left", padx=5)

ttk.Label(root, text="Result").grid(row=3, column=0, sticky="e")
res = ttk.Entry(root, width=40)
res.grid(row=3, column=1, padx=8, pady=(0, 12))

root.mainloop()

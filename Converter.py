import tkinter as tk

def convert_to_m():
    try:
        cm = float(cm_entry.get())
        m = cm / 100
        result_label.config(text=f"{cm} cm = {m} m")
    except ValueError:
        result_label.config(text="Invalid input")

def convert_to_cm():
    try:
        m = float(m_entry.get())
        cm = m * 100
        result_label.config(text=f"{m} m = {cm} cm")
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Converter")

cm_label = tk.Label(root, text="cm")
cm_label.grid(row=0, column=0)

cm_entry = tk.Entry(root)
cm_entry.grid(row=0, column=1)

to_m_button = tk.Button(root, text="Convert to m", command=convert_to_m)
to_m_button.grid(row=0, column=2)

m_label = tk.Label(root, text="m")
m_label.grid(row=1, column=0)

m_entry = tk.Entry(root)
m_entry.grid(row=1, column=1)

to_cm_button = tk.Button(root, text="Convert to cm", command=convert_to_cm)
to_cm_button.grid(row=1, column=2)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3)

root.mainloop()
import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S')
    label.config(text=current_time)
    label.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Customize the label for the clock
label = tk.Label(root, font=('Helvetica', 48), background='black', foreground='white')
label.pack(anchor='center')

# Start the clock
update_time()

# Run the application
root.mainloop()

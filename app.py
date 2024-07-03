import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        text_area.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text_area.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def about():
    messagebox.showinfo("About", "Simple Notepad using Python Tkinter")

# Set up the main application window
root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

# Create a text area
text_area = tk.Text(root, wrap='word')
text_area.pack(expand='yes', fill='both')

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Add File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save As...", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Run the application
root.mainloop()

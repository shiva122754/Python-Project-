import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
app = tk.Tk()
app.title("Simple GUI Application")

# Create and add widgets to the window
label = tk.Label(app, text="Enter your name:")
label.pack(pady=10)

entry = tk.Entry(app)
entry.pack(pady=10)

button = tk.Button(app, text="Say Hello", command=on_button_click)
button.pack(pady=10)

# Start the main event loop
app.mainloop()
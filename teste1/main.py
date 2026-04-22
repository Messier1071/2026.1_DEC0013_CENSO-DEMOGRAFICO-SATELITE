import tkinter as tk

def test():
    print("Hello World!")
# Create the main application window
root = tk.Tk()
root.title("Hello Tkinter")

# Add a text label
label = tk.Label(root, text="Welcome to Python GUI!")
label.pack(pady=10)

# Add a quit button
button = tk.Button(root, text="Quit", command=root.destroy)
button.pack(pady=5)

button2 = tk.Button(root, text="test", command=test)
button2.pack(pady=7)


# Start the event loop
root.mainloop()

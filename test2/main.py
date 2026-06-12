import tkinter as tk
from PIL import Image, ImageTk
import cv2

def test():
    print("Hello World!")
# Create the main application window
root = tk.Tk()
root.title("Hello Tkinter")

# Add a quit button
button = tk.Button(root, text="Quit", command=root.destroy)
button.pack(pady=5)

# Load the image using Pillow
image = Image.open("images/image.png")
# Convert to a Tkinter-compatible photo object
tmp = cv2.imread("images/image.png",0)
photo = ImageTk.PhotoImage(tmp)

# Create a label to hold the image
label = tk.Label(root, image=photo)
label.pack()

# IMPORTANT: Keep a reference to avoid garbage collection
label.image = photo

# Start the event loop
root.mainloop()


root = tk.Tk()

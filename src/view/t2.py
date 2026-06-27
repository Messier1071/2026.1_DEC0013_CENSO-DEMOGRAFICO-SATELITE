import tkinter as tk
from tkinter import ttk

# 1. Create the main application window
root = tk.Tk()
root.title("Tkinter Tabs Example")
root.geometry("400x300")

# 2. Create the Notebook widget (the tab container)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# 3. Create frames for each individual tab
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# 4. Add the frames to the notebook with text labels
notebook.add(tab1, text="Profile Setup")
notebook.add(tab2, text="Application Settings")

# 5. Add unique widgets inside Tab 1 (make tab1 the master)
label1 = ttk.Label(tab1, text="Enter your user profile details here.")
label1.pack(padx=20, pady=20)
button1 = ttk.Button(tab1, text="Save Profile")
button1.pack()

# 6. Add unique widgets inside Tab 2 (make tab2 the master)
label2 = ttk.Label(tab2, text="Configure your system preferences.")
label2.pack(padx=20, pady=20)
check_btn = ttk.Checkbutton(tab2, text="Enable Dark Mode")
check_btn.pack()

# Start the application loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox
import os
import json

# Function to create a new folder in the PROJECT directory
def create_folder(folder_name):
    folder_path = os.path.join("projects", folder_name)

    # Create the folder if it does not exist
    os.makedirs(folder_path, exist_ok=True)

    messagebox.showinfo("Folder Created", f"Folder '{folder_name}' created successfully!")

    # Save the folder name in folder.json
    json_data = {}

    # Load existing data from folder.json if it exists
    json_path = os.path.join("projects", "folder.json")
    if os.path.exists(json_path):
        with open(json_path, 'r') as json_file:
            json_data = json.load(json_file)

    # Update the JSON data with the new folder name
    json_data[folder_name] = folder_path

    # Save the updated data to folder.json
    with open(json_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

# Function to handle button click event
def create_folder_button():
    folder_name = entry.get()

    # Validate folder name
    if not folder_name:
        messagebox.showerror("Error", "Please enter a folder name!")
        return

    create_folder(folder_name)
    entry.delete(0, tk.END)  # Clear the entry field after creating the folder

# Create the Tkinter window
window = tk.Tk()
window.title("New Folder")
window.geometry("300x150")

# Create label and entry for folder name
label = tk.Label(window, text="Enter Folder Name:")
label.pack()
entry = tk.Entry(window, width=30)
entry.pack()

# Create button to create folder
button = tk.Button(window, text="Create Folder", command=create_folder_button)
button.pack()

# Run the Tkinter event loop
window.mainloop()

import requests
import tkinter as tk
from tkinter import messagebox

def perform_whois_lookup():
    domain = entry.get()
    
    # Make a request to the WHOIS API
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?domainName={domain}&apiKey= at_hvTajLDWhlUG1EfLUu1q3uz6rOiEw"
    response = requests.get(url)
    
    if response.status_code == 200:
        result = response.text
        
        # Clear previous output
        output.delete('1.0', tk.END)
        
        # Update the output text box with the retrieved information
        output.insert(tk.END, result)
    else:
        messagebox.showerror('Error', 'WHOIS lookup failed. Please check your internet connection.')

# Create the Tkinter window
window = tk.Tk()
window.title("WHOIS Lookup")
window.geometry("400x300")
window.configure(bg="white")

# Create the domain entry text box
entry = tk.Entry(window, width=30)
entry.pack(pady=20)

# Create the search button
button = tk.Button(window, text="Search", command=perform_whois_lookup)
button.pack()

# Create the output area
output = tk.Text(window, bg="white", fg="black")
output.pack(pady=20)

# Run the Tkinter event loop
window.mainloop()

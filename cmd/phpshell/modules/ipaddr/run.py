import json
import requests
import tkinter as tk
from tkinter import messagebox

def get_ip_info():
    # Load the API key from api.json file
    with open('api.json') as file:
        api_data = json.load(file)
        api_key = api_data['api_key']

    # Get the IP address from the input field
    ip_address = ip_entry.get()

    # Make a request to the IPinfo API
    url = f'https://ipinfo.io/{ip_address}?token={api_key}'
    response = requests.get(url)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract relevant information
        ip = data.get('ip')
        city = data.get('city')
        region = data.get('region')
        country = data.get('country')
        org = data.get('org')

        # Clear the output text box
        output_text.delete('1.0', tk.END)

        # Update the output text box with the retrieved information
        output_text.insert(tk.END, f'IP: {ip}\n')
        output_text.insert(tk.END, f'City: {city}\n')
        output_text.insert(tk.END, f'Region: {region}\n')
        output_text.insert(tk.END, f'Country: {country}\n')
        output_text.insert(tk.END, f'Organization: {org}\n')
    else:
        messagebox.showerror('Error', 'Error occurred while retrieving IP information.')



# Create the tkinter window
window = tk.Tk()
window.title('IP LOOKUP')
window.geometry('400x300')
window.configure(background='black')

# Create the IP entry field
ip_entry = tk.Entry(window, width=30)
ip_entry.pack(pady=20)

# Create the Get button
get_button = tk.Button(window, text='Get', command=get_ip_info, bg='blue', fg='white')
get_button.pack()

# Create the output text box
output_text = tk.Text(window, bg='black', fg='blue')
output_text.pack(pady=20)

# Create the status bar


# Run the tkinter event loop
window.mainloop()

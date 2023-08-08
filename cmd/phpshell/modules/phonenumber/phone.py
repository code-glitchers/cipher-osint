import json
import csv
import tkinter as tk
import tkinter.ttk as ttk
import requests
from phonenumbers import parse, is_valid_number
from opencage.geocoder import OpenCageGeocode

def fetch_phone_info():
    mobileno = phone_entry.get()

    try:
        parsed_number = parse(mobileno)
    except:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "[!] Please add '+' sign to the country code")
        return

    if not is_valid_number(parsed_number):
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "[!] You have entered an invalid phone number!")
        return

    try:
        with open('api.json', 'r') as json_file:
            data = json.load(json_file)
            apilayer_api = data['apilayer_api']
    except FileNotFoundError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "[!] api.json file not found or API key not specified!")
        return

    api_url = f"http://apilayer.net/validate?access_key={apilayer_api}&number={mobileno}&format=1"
    response = requests.get(api_url)

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, f"[~] Phone Number Details:\n\nTarget Number  : {mobileno}\nStatus Code    : {response.status_code}\n\n")

    try:
        phone_details = response.json()
        for key, value in phone_details.items():
            result_text.insert(tk.END, f"{key.capitalize()}{' ' * (14 - len(key))}: {value}\n")
    except KeyError:
        result_text.insert(tk.END, "[!] Some phone details are not available")

def save_results():
    results = result_text.get(1.0, tk.END)
    if not results:
        return

    save_format = save_format_var.get()
    if save_format == "JSON":
        with open('phone_results.json', 'w') as json_file:
            json_file.write(results)
        result_text.insert(tk.END, "\n[+] Results saved as JSON: phone_results.json")
    elif save_format == "HTML":
        with open('phone_results.html', 'w') as html_file:
            html_file.write(f"<pre>{results}</pre>")
        result_text.insert(tk.END, "\n[+] Results saved as HTML: phone_results.html")
    elif save_format == "CSV":
        csv_rows = [line.strip().split(':') for line in results.split('\n') if line.strip()]
        with open('phone_results.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_rows)
        result_text.insert(tk.END, "\n[+] Results saved as CSV: phone_results.csv")

# Create the main window
window = tk.Tk()
window.title("Phone Number Info")
window.geometry("1000x1000")
window.configure(bg="#1f1f1f")

# Style for dark mode
style = ttk.Style()
style.theme_use("clam")
style.configure(".", background="#1f1f1f", foreground="#f2f2f2", font=("Arial", 10))
style.configure("TLabel", background="#1f1f1f", foreground="#f2f2f2")
style.configure("TEntry", fieldbackground="#f2f2f2", foreground="#1f1f1f")
style.configure("TButton", background="#333333", foreground="#f2f2f2", activebackground="#555555", activeforeground="#f2f2f2")
style.configure("TRadiobutton", background="#1f1f1f", foreground="#f2f2f2")

# Phone number entry
phone_label = ttk.Label(window, text="Enter phone number:")
phone_label.pack()

phone_entry = ttk.Entry(window)
phone_entry.pack()

# Fetch API button
fetch_button = ttk.Button(window, text="search", command=fetch_phone_info)
fetch_button.pack()

# Result text box
result_text = tk.Text(window)
result_text.pack()

# Save format selection
save_format_label = ttk.Label(window, text="Select save format:")
save_format_label.pack()

save_format_var = tk.StringVar(window, "JSON")

save_format_radio_json = ttk.Radiobutton(window, text="JSON", variable=save_format_var, value="JSON")
save_format_radio_json.pack(anchor="w")

save_format_radio_html = ttk.Radiobutton(window, text="HTML", variable=save_format_var, value="HTML")
save_format_radio_html.pack(anchor="w")

save_format_radio_csv = ttk.Radiobutton(window, text="CSV", variable=save_format_var, value="CSV")
save_format_radio_csv.pack(anchor="w")

# Save button
save_button = ttk.Button(window, text="Save Results", command=save_results)
save_button.pack()

# Start the Tkinter event loop
window.mainloop()

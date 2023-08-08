import requests
import tkinter as tk
from tkinter import messagebox

def get_ip_info():
    ip_address = ip_entry.get()

    url = f'https://ipapi.co/{ip_address}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        ip = data.get('ip')
        city = data.get('city')
        region = data.get('region')
        country = data.get('country_name')
        org = data.get('org')

        output_text.delete('1.0', tk.END)
        output_text.insert(tk.END, f'IP: {ip}\n')
        output_text.insert(tk.END, f'City: {city}\n')
        output_text.insert(tk.END, f'Region: {region}\n')
        output_text.insert(tk.END, f'Country: {country}\n')
        output_text.insert(tk.END, f'Organization: {org}\n')
    else:
        messagebox.showerror('Error', 'Error occurred while retrieving IP information.')

def save_results():
    results = output_text.get('1.0', tk.END)
    if not results:
        return

    save_format = save_format_var.get()
    if save_format == 'JSON':
        with open('ip_results.json', 'w') as json_file:
            json_file.write(results)
        messagebox.showinfo('Saved', 'Results saved as JSON: ip_results.json')
    elif save_format == 'HTML':
        with open('ip_results.html', 'w') as html_file:
            html_file.write(f'<pre>{results}</pre>')
        messagebox.showinfo('Saved', 'Results saved as HTML: ip_results.html')
    elif save_format == 'CSV':
        rows = results.strip().split('\n')
        headers = [row.split(':')[0].strip() for row in rows]
        data = [row.split(':')[1].strip() for row in rows]
        rows = [headers, data]

        with open('ip_results.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(rows)
        messagebox.showinfo('Saved', 'Results saved as CSV: ip_results.csv')

window = tk.Tk()
window.title('IP Lookup')
window.geometry('800x800')
window.configure(background='black')

ip_entry = tk.Entry(window, width=30)
ip_entry.pack(pady=20)

get_button = tk.Button(window, text='Get', command=get_ip_info)
get_button.pack()

output_text = tk.Text(window, bg='white', fg='black')
output_text.pack(pady=20)

save_format_var = tk.StringVar(window, 'JSON')

save_format_radio_json = tk.Radiobutton(window, text='JSON', variable=save_format_var, value='JSON')
save_format_radio_json.pack(anchor='w')

save_format_radio_html = tk.Radiobutton(window, text='HTML', variable=save_format_var, value='HTML')
save_format_radio_html.pack(anchor='w')

save_format_radio_csv = tk.Radiobutton(window, text='CSV', variable=save_format_var, value='CSV')
save_format_radio_csv.pack(anchor='w')

save_button = tk.Button(window, text='Save Results', command=save_results)
save_button.pack()

window.mainloop()

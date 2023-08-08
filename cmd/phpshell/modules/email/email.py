import requests

def gather_email_details(email_address):
    api_key = 'wwyE3uKj'
    url = f'https://api.neverbounce.com/v4/single/check?key={api_key}&email={email_address}'

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get('result') == 'valid':
            details = {
                'email': data['email'],
                'result': data['result'],
                'flags': data['flags'],
                'suggested_correction': data.get('suggested_correction')
            }
            return details
    
    return None

# Example usage
email = 'techdenlab@gmail.com'
details = gather_email_details(email)
if details:
    print(details)
else:
    print("Failed to gather email details.")

import requests

url = 'https://api.exchangerate-api.com/v4/latest/USD'  

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    print("Base Currency:", data['base'])
    print("Exchange Rates:")
    for currency, rate in data['rates'].items():
        print(f"{currency}: {rate}")
else:
    print("Failed to retrieve data:", response.status_code)

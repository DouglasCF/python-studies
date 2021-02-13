import requests
import json

url = 'https://api.wazirx.com/api/v2/tickers/btcusdt'
price_notifier = 45000.0

response = requests.get(url)
json_data = json.loads(response.text)

last = float(json_data['ticker']['last'])

if last <= price_notifier:
    print('Buy')

print(f'Bitcoin price: {last}')

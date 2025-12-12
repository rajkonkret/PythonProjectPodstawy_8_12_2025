import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/"

response = requests.get(url)
print(response)

data = response.json()
print(data)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
# 'rates': [{'no': '241/A/NBP/2025', 'effectiveDate': '2025-12-12', 'mid': 4.2271}]}
print(data['rates'])
print(data['rates'][0])
print(data['rates'][0]['mid'])  # 4.2271

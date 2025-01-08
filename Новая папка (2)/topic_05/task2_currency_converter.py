
import requests

def get_exchange_rate(currency_code):
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency_code}&json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['rate']
    return None

if __name__ == "__main__":
    currencies = {"EUR": "Euro", "USD": "US Dollar", "PLN": "Polish Zloty"}
    amount = float(input("Enter amount: "))
    currency = input(f"Enter currency ({', '.join(currencies.keys())}): ").upper()
    if currency in currencies:
        rate = get_exchange_rate(currency)
        if rate:
            print(f"{amount} {currency} = {amount * rate:.2f} UAH")
        else:
            print("Failed to fetch exchange rate.")
    else:
        print("Unsupported currency.")

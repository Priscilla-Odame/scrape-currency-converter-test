from bs4 import BeautifulSoup as bs
import requests
import json

data_file=[]

def convert_page(amount, from_currency, to_currency):
    try:
        url = f'https://wise.com/gb/currency-converter/{from_currency}-to-{to_currency}-rate?amount={amount}'

        response = requests.get(url).text
        data = bs(response, "html.parser")

        rate = data.find("span", class_="text-success").text.strip()
        time_data = data.find("small", class_="m-r-1").text.split()
        time_of_conversion = time_data[4]
        timezone = time_data[5]
        converted_amount = amount * float(rate)

        result = {
            "converted_amount": converted_amount,
            "rate": float(rate),
            "metadata": {
                "time_of_conversion": f'{time_of_conversion} {timezone}',
                "from_currency": from_currency.upper(),
                "to_currency": to_currency.upper()
            }
        }

        
        with open('data.json', 'w+') as f:
            data_file.append(result)
            json.dump(data_file, f, indent=4)
        f.close()

        return result
    except:
        return {"error": "Please enter valid parameters. It should be amount(float), from_currency(str eg:usd) and to_currency(str eg:eur). Please use http://127.0.0.1:8000/currencies?api_key=value to check supported currencies"}

def get_currencies():
    url = f'https://wise.com/gb/currency-converter/currencies'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers).text
    data = bs(response, 'html.parser')

    codes = data.find_all("h5", class_='currencies_currencyCard__currencyCode__RG8bp')
    currency_codes = [code.text for code in codes]

    names = data.find_all("p", class_='currencies_currencyCard__currencyName__wj5_u')
    currency_names = [name.text for name in names]

    result = {currency_names[i]: currency_codes[i] for i in range(len(currency_names))}

    return result


def get_history():
    try:
        with open('data.json', 'r') as f:
            data_file = json.load(f)
        return data_file
    except:
        return {"message": "There is no history yet..."}

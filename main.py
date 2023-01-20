from fastapi import FastAPI
from web_scrape import convert_page, get_currencies, get_history


app = FastAPI()

@app.get('/convert/{amount}/{from_currency}/{to_currency}')
def convert_currency(amount:float, from_currency: str, to_currency: str):
    result = convert_page(amount, from_currency, to_currency)
    return result


@app.get('/currencies')
async def get_all_currencies():
    result = get_currencies()
    return result

@app.get('/history')
def get_conversion_history():
    result = get_history()
    return result
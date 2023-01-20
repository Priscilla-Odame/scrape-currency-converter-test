from fastapi import FastAPI, Depends
from web_scrape import convert_page, get_currencies, get_history
import auth_api
from fastapi.security.api_key import APIKey


app = FastAPI()

@app.get('/convert/{amount}/{from_currency}/{to_currency}')
def convert_currency(amount:float, from_currency: str, to_currency: str ,api_key:APIKey = Depends(auth_api.get_api_key)):
    result = convert_page(amount, from_currency, to_currency)
    return result


@app.get('/currencies')
async def get_all_currencies(api_key:APIKey = Depends(auth_api.get_api_key)):
    result = get_currencies()
    return result

@app.get('/history')
def get_conversion_history(api_key:APIKey = Depends(auth_api.get_api_key)):
    result = get_history()
    return result
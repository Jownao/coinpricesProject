import requests, random
import time

def get_crypto_price(crypto, currency='usd', fake=False):
    if fake:
        # Gerar um preço falso entre 10 e 1000
        return round(random.uniform(10, 1000), 2)
    else:
        url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}'
        response = requests.get(url)
        time.sleep(3)
        data = response.json()
        if crypto in data and currency in data[crypto]:
            return data[crypto][currency]
        else:
            print(f'Preço não disponível para {crypto} em {currency}')
            return None

def get_usd_to_brl(fake=False):
    if fake:
        # Gerar um valor falso para o USD em BRL entre 4 e 6
        return round(random.uniform(4, 6), 2)
    else:
        time.sleep(3)
        return get_crypto_price('usd', 'brl')
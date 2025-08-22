import requests
from datetime import datetime
import pandas as pd

def get_bitcoin_df() -> pd.DataFrame:
    url= 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    data = response.json()
    print(data)

    #Extract the data
    price = data['data']['amount']
    currency = data['data']['currency']
    ticker = data['data']['base']
    timestamp = datetime.now()

    # Create df
    df = pd.DataFrame([{
        'ticker': ticker,
        'price': price,
        'currency': currency,
        'timestamp': timestamp
    }])

    return df

if __name__ == "__main__":
    df = get_bitcoin_df()
    print(df)
    print("Successfully done!")
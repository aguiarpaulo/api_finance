import yfinance as yf
import pandas as pd
from datetime import datetime

def get_commodities_df() -> pd.DataFrame:
    symbols = ["GC=F", "CL=F", "SI=F"]
    dfs = []

    for sym in symbols:
        ultimo_df = yf.Ticker(sym).history(period="1d", interval="1m")[["Close"]].tail(1)

        # Renaming columns
        ultimo_df = ultimo_df.rename(columns={"Close": "price"})
        ultimo_df["ticker"] = sym
        ultimo_df["currency"] = "USD"
        ultimo_df["timestamp"] = datetime.now()

        # Ordering columns
        ultimo_df = ultimo_df[["ticker", "price", "currency", "timestamp"]]

        dfs.append(ultimo_df)

    # Concat in one df
    return pd.concat(dfs, ignore_index=True)


if __name__ == "__main__":
    df = get_commodities_df()
    print(df)
    print("Successfully done!")
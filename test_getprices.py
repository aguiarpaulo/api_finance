import pandas as pd
from api_bitcoin import get_bitcoin_df
from get_commodities import get_commodities_df

if __name__ == "__main__":
    df_btc = get_bitcoin_df()
    df_comm = get_commodities_df()

    # concat all
    df = pd.concat([df_btc,df_comm], ignore_index=True)

    print(df)
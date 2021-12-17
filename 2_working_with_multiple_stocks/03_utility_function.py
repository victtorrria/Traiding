import os
import pandas as pd

def symbol_to_path(symbol, base_dir='data'):
    """Return CSV file path to given ticker symbol"""
    return os.path.join(base_dir, f'{symbol}.csv')

def get_data(symbols, dates):
    """Return stock data (Adj Close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'AAPL' not in symbols:
        symbols.insert(0, 'AAPL')

    for symbol in symbols:
        df_temp = pd.read_csv(
           symbol_to_path(symbol),
           index_col='Date',
           parse_dates=True,
           usecols=['Date', 'Adj Close'],
           na_values=['nan']           
        )
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        df = df.dropna()

    return df

def main():
    dates = pd.date_range('2020-01-01', '2020-01-31')
    symbols = ['AMZN', 'GOOG']
    df = get_data(symbols, dates)
    print(df.head())

if __name__=='__main__':
    main()



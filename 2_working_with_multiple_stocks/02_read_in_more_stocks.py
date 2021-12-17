import pandas as pd

def main():
    start_date = '2021-01-08'
    end_date = '2021-01-15'
    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)
    dfAAPL = pd.read_csv('data/AAPL.csv',
                         index_col='Date',
                         parse_dates=True,
                         usecols=['Date', 'Adj Close'])

    dfAAPL = dfAAPL.rename(columns={'Adj Close': 'AAPL'})
    df1 = df1.join(dfAAPL, how = 'inner').dropna()

    symbols = ['AMZN', 'GOOG']
    for symbol in symbols:
        df_temp = pd.read_csv(f'data/{symbol}.csv', index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])

        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp)
        
    print(df1)

if __name__=='__main__':
    main()



    
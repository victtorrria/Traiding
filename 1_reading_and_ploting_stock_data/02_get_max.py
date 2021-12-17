import pandas as pd

def get_max_close(symbol):
    df = pd.read_csv(('data/{}.csv').format(symbol))
    return df['Close'].max()

def main():
    print('Max Close:')
    for symbol in ['AAPL', 'AMZN', 'GOOG']:
        print(symbol + ":", get_max_close(symbol))

if __name__ == "__main__":
    main()
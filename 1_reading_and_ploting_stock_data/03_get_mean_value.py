import pandas as pd

def get_mean_volume(symbol):
    df = pd.read_csv(('data/{}.csv').format(symbol))
    return df['Volume'].mean

def main():
    print('Mean Volume')
    for symbol in ['AAPL', 'AMZN', "GOOG"]:
        print(symbol + ": ", get_mean_volume(symbol))

if __name__=="__main__":
    main()






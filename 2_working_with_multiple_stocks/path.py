import os
import pandas as pd

def symbol_to_path(symbol, base_dir='data'):
    """Return CSV file path to given ticker symbol"""
    return os.path.join(base_dir, f'{symbol}.csv')

print(symbol_to_path('AAPL'))
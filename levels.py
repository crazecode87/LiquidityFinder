import pandas as pd
from collections import defaultdict

def find_frequent_levels(cleaned_file_path,threshold, rounding, top_n) -> list[float]:
    df = pd.read_csv(cleaned_file_path)
    price_columns = ['Open', 'High', 'Low', 'Close']
    all_prices = []

    for col in price_columns:
        rounded = df[col].apply(lambda x: round(x / rounding) * rounding)
        all_prices.extend(rounded)

    freq = defaultdict(int)
    for price in all_prices:
        freq[price] += 1

    top_prices = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_n]
    levels = [round(p[0], 2) for p in top_prices]
    return levels
import pandas as pd
from collections import defaultdict

def find_frequent_levels(cleaned_file_path, threshold, top_n) -> list[float]:
    df = pd.read_csv(cleaned_file_path)

    # Reverse and take the most recent top_n rows
    #df = df[::-1].head(top_n)

    price_columns = ['Open', 'High', 'Low', 'Close']
    all_prices = []

    for col in price_columns:
        all_prices.extend(df[col])

    # Count exact price occurrences without rounding
    freq = defaultdict(int)
    for price in all_prices:
        freq[price] += 1

    # Sort by frequency and get top N candidates
    top_prices = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Filter out nearby clusters (within threshold of each other)
    refined_levels = []
    for price, _ in top_prices:
        if all(abs(price - existing) > threshold for existing in refined_levels):
            refined_levels.append(price)
        if len(refined_levels) >= top_n:
            break

    return refined_levels
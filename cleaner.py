import pandas as pd
import re
import os

def clean_ohlc_data(input_file, output_file):
    # Expected column layout from the exported CSV
    column_names = [
        "Index", "Strategy", "Action", "Qty", "UnderlyingPrice", "DateTime",
        "Profit", "RunningTotal", "Multiplier", "Unused"
    ]

    # Load CSV, skipping the first 10 lines
    df = pd.read_csv(input_file, sep=';', skiprows=10, names=column_names, encoding='utf-8')

    # Filter only OHLC rows
    ohlc_rows = df[df['Strategy'].str.contains(r'\(OHLC\|', na=False)].copy()

    # Extract OHLC values
    ohlc_rows[['Open', 'High', 'Low', 'Close']] = ohlc_rows['Strategy'].str.extract(
        r'\(OHLC\|([0-9.]+)\|([0-9.]+)\|([0-9.]+)\|([0-9.]+)\)'
    ).astype(float).round(2)

    # take only the desired columns
    cleaned_df = ohlc_rows[['DateTime', 'Open', 'High', 'Low', 'Close']]

    # Convert DateTime column
    cleaned_df['DateTime'] = pd.to_datetime(cleaned_df['DateTime'])

    # Save cleaned data
    cleaned_df.to_csv(output_file, index=False)
    print(f"Cleaned file saved as: {output_file}")
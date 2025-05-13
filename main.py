# main.py

import os
import pandas as pd

from cleaner import clean_ohlc_data
from levels  import find_frequent_levels
from charts  import plot_chart

def process_file(raw_path, cleaned_folder, levels_folder,
                 rounding=0.05, top_n=20, threshold=0.15):
    """
    CSV file processing for data export from the thinkorswim platform
    1. Clean raw CSV > cleaned_folder
    2. Compute levels > list of price points
    3. Save levels to levels_folder
    4. Plot chart with those levels
    """
    base = os.path.splitext(os.path.basename(raw_path))[0]

    # Clean
    cleaned_name = f"{base}_cleaned.csv"
    cleaned_path = os.path.join(cleaned_folder, cleaned_name)
    clean_ohlc_data(raw_path, cleaned_path)

    # Find levels 
    levels_list = find_frequent_levels(
        cleaned_path,
        threshold=threshold,
        rounding=rounding,
        top_n=top_n
    )

    #  Save levels CSV
    levels_name = f"{base}_levels.csv"
    levels_path = os.path.join(levels_folder, levels_name)
    pd.DataFrame({'Level': levels_list}).to_csv(levels_path, index=False)
    print(f"Wrote {len(levels_list)} levels to {levels_path}")

    # Plot chart 
    title = f"{base} Chart with Liquidity Levels"
    plot_chart(cleaned_path, levels_list, title=title)

def main():
    raw_folder     = "rawData"
    cleaned_folder = "cleaned"
    levels_folder  = "levels"

    # check if output folders exist
    os.makedirs(cleaned_folder, exist_ok=True)
    os.makedirs(levels_folder,  exist_ok=True)

    # process each CSV file
    for fname in os.listdir(raw_folder):
        if not fname.lower().endswith(".csv"):
            continue
        raw_path = os.path.join(raw_folder, fname)
        process_file(raw_path, cleaned_folder, levels_folder)

    print("All files processed.")

if __name__ == "__main__":
    main()
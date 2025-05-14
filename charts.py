import os
import pandas as pd
import mplfinance as mpf

def plot_chart(cleaned_file_path: str, levels: list, title: str = None):
    """
    Plot a candlestick chart of cleaned OHLC data with horizontal lines at specified price levels.

    Parameters:
    - cleaned_file_path: Path to the cleaned CSV (must contain 'DateTime', 'Open', 'High', 'Low', 'Close').
    - levels: List of price levels (floats) to draw as horizontal lines.
    """
    # Load cleaned data
    df = pd.read_csv(cleaned_file_path)
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    df.set_index('DateTime', inplace=True)

    # Use filename as default title if none provided
    chart_title = title or os.path.basename(cleaned_file_path)

    # Prepare horizontal line settings
    hlines = {
        'hlines': levels,
        'colors': 'orange',
        'linestyle': 'dashed',
        'linewidths': 1
    }

    # Plot
    mpf.plot(
        df,
        type='candle',  # Alt: 'candle', 'line', 'renko', 'pnf'
        style='nightclouds',  # Alt: 'default', 'yahoo', 'nightclouds', etc.
        title=chart_title,
        hlines=hlines,
        volume=False,  # if you want volume subplot
        #mav=(5, 10, 20),  # Show moving averages
        
    )

# Tick Inspector (OHLCV Data Auditor)

A standalone Python CLI application designed to audit historical financial market data for structural integrity and mathematical accuracy. Tick Inspector acts as a quality assurance layer, ensuring data is clean before being fed into algorithmic trading models or backtesting engines.

Looking to download crypto data? You can do it from Yahoo Finance using my script [here](https://github.com/priyanshsx/learning-python/tree/main/ohlcv_downloader)! 

## Features

* **Fail-Safe File Loading:** Uses infinite loop and `try/except` logic to prevent crashes from typos when users input file paths.
* **Chronological Audit:** Rebuilds the time series physics to automatically detect duplicate timestamps and identify missing trading days.
* **Market Physics Validation:** Uses Boolean masking to flag mathematically impossible rows, including:
  * Low prices exceeding High prices.
  * Open or Close prices exceeding the day's High.
  * Negative trading volume.
* **Smart Reporting:** Generates a clean, high-level Data Health Report in the terminal, only printing raw corrupted DataFrames if an error is actually detected.

## Setup & Usage

1. **Install Dependencies:**
   This project requires Pandas for advanced data manipulation. Install it via your terminal:
   `pip install pandas`
2. **Run the Script:**
   Execute the `auditor.py` (or your chosen filename) script in your terminal.
3. **Follow the Prompt:**
   Enter the exact name of the `.csv` file you wish to inspect (e.g., `BTC-USD.csv`). The file must be in the same directory as the script or include the full file path. 
   *(Note: The CSV must contain standard OHLCV columns and a 'date' column).*
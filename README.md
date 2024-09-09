# XLS Stacking

This project provides tools for converting XLS files to CSV, stacking multiple CSV files, and converting the combined result back to XLS format.

## Features

- Convert XLS files to CSV format
- Stack multiple CSV files into a single CSV file
- Convert the combined CSV file back to XLS format
- Preserve the orientation of data (keys as rows, file names as columns)

## Requirements

- Python 3.8+
- pandas
- openpyxl

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/gv-sh/xls-stacking.git
   cd xls-stacking
   ```

2. Install the required packages:
   ```
   pip install pandas openpyxl
   ```

## Usage

1. Place your XLS files in the `input/` directory.

2. Run the Jupyter notebook `csv_stacking.ipynb`:
   - This will convert XLS files to CSV, stack them, and create a combined output.

3. The combined output will be saved as `combined_output.csv` in the project directory.

4. To convert the combined CSV back to XLS format, use the `csv2xls.py` script.

## File Descriptions

- `xls2csv.py`: Script to convert XLS files to CSV format
- `csv2xls.py`: Script to convert CSV files to XLS format
- `csv_stacking.ipynb`: Jupyter notebook that orchestrates the entire process

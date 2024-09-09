import os
import pandas as pd
from pathlib import Path

def convert_csv_to_xls(input_dir, output_dir):
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    converted_files = []

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.xls'
            output_path = os.path.join(output_dir, output_filename)

            # Read the CSV file
            df = pd.read_csv(input_path, header=None, names=['Key', 'Value'])

            # Write to XLS
            df.to_excel(output_path, index=False, header=False, engine='openpyxl')
            converted_files.append(output_filename)
            print(f"Converted {filename} to {output_filename}")

    print("Conversion complete.")
    return converted_files

# This allows the script to be run standalone if needed
if __name__ == "__main__":
    input_directory = 'csv_input/'  # Directory containing CSV files
    output_directory = 'xls_output/'  # Directory to store converted XLS files
    convert_csv_to_xls(input_directory, output_directory)

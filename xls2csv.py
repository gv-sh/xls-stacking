import os
import pandas as pd
from pathlib import Path

def convert_xls_to_csv(input_dir, output_dir):
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    converted_files = []

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.xls', '.xlsx')):
            input_path = os.path.join(input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.csv'
            output_path = os.path.join(output_dir, output_filename)

            # Read the Excel file
            df = pd.read_excel(input_path, header=None, names=['Key', 'Value'])

            # Write to CSV
            df.to_csv(output_path, index=False)
            converted_files.append(output_filename)
            print(f"Converted {filename} to {output_filename}")

    print("Conversion complete.")
    return converted_files

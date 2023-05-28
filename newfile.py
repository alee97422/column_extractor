import pandas as pd
import argparse

def separate_columns(csv_file, selected_columns):
    data = pd.read_csv(csv_file)
    separated_data = data[selected_columns]
    return separated_data.head(100000)

def save_csv(data, output_file):
    data.to_csv(output_file, index=False)

def save_xlsx(data, output_file):
    data.to_excel(output_file, index=False)

def main():
    parser = argparse.ArgumentParser(description="CSV Column Separator")
    parser.add_argument("csv_file", help="Path to the CSV file")
    parser.add_argument("selected_columns", nargs='+', help="Columns to separate")
    parser.add_argument("--output_file", help="Output file name")
    parser.add_argument("--format", choices=["csv", "xlsx"], default="csv", help="Output file format (csv or xlsx)")

    args = parser.parse_args()

    csv_file = args.csv_file
    selected_columns = args.selected_columns
    output_file = args.output_file
    file_format = args.format

    separated_data = separate_columns(csv_file, selected_columns)

    print("Separated Data:")
    print(separated_data)

    if output_file is not None:
        if file_format == "csv":
            save_csv(separated_data, output_file)
        elif file_format == "xlsx":
            save_xlsx(separated_data, output_file)
        print(f"Separated data saved as {file_format.upper()} file: {output_file}")

if __name__ == '__main__':
    main()

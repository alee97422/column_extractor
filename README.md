# CSV Column Separator

This program allows you to separate specific columns from a CSV file and save the separated data as either a CSV or XLSX file. It provides a command-line interface (CLI) for easy execution.

## Dataset

The program assumes that you have a chess game dataset in CSV format. You can download the dataset from Kaggle by clicking here > [![Kaggle Chess Game Dataset](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)]([https://www.kaggle.com/datasnaek/chess](https://www.kaggle.com/datasets/ulrikthygepedersen/online-chess-games))

Please ensure you have downloaded and saved the dataset in a suitable location before using the program.

## Prerequisites

Before running the program, make sure you have Python (version 3 or above) installed on your system. You also need to install the required libraries by running the following command:

pip install pandas openpyxl

## Usage

To use the program, follow these steps:

1. Open a command-line interface (CLI) or terminal.

2. Navigate to the directory where the program file (csv_column_separator.py) is located.

3. Run the following command to execute the program and separate the desired columns from the CSV file:

python csv_column_separator.py <csv_file> <selected_columns> [--output_file <output_file>] [--format <format>]

Replace the placeholders with the appropriate values:
- <csv_file>: Path to the CSV file you want to process (e.g., chess_games.csv).
- <selected_columns>: Names of the columns you want to separate, separated by spaces (e.g., turns victory_status).
- <output_file> (optional): Desired output file name (default is output.csv).
- <format> (optional): Output file format, either csv or xlsx (default is csv).

4. The program will display a snippet of the separated data and save the output file in the specified format.

Please note that if you don't provide the --output_file and --format options, the program will display the separated data but won't save it as a separate file.

## Examples

Separating "turns" and "victory_status" columns from the CSV file "chess_games.csv" and saving the output as "output.csv" in CSV format:
python csv_column_separator.py chess_games.csv turns victory_status --output_file output.csv --format csv

Separating "turns" and "victory_status" columns from the CSV file "chess_games.csv" and saving the output as "output.xlsx" in XLSX format:
python csv_column_separator.py chess_games.csv turns victory_status --output_file output.xlsx --format xlsx

Please make sure to adjust the command based on your specific file paths and column names.

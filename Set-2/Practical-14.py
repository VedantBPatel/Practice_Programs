import csv

def calculate_column_average(file_path, column_name):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)

            values = []
            
            for row in reader:
                if column_name in row and row[column_name].strip().isdigit():
                    values.append(float(row[column_name].strip()))
            
            if values:
                average = sum(values) / len(values)
                return f"The average of the column '{column_name}' is: {average}"
            else:
                return f"No numeric values found in the column '{column_name}'."
    except FileNotFoundError:
        return "The specified file could not be found."
    except KeyError:
        return f"The column '{column_name}' does not exist in the file."

# Example usage:
file_path = "Practice_Programs/Set-2/student_marksheet.csv"  # Replace with the path to your CSV file
column_name = "Fees"  # Replace with the target column name

print(calculate_column_average(file_path, column_name))

"""
csv.DictReader(file):

This reads the content of the CSV file (file) and interprets each row as an ordered dictionary.

The dictionary's keys are the column headers from the CSV file (the first row).

The dictionary's values are the data in the corresponding columns for each row in the CSV.
"""

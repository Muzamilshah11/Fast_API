import csv

# Data for the Employee_Data table
data = [
    {"emp_id": 1, "emp_name": "John Doe", "emp_phone": "1234567890", "emp_address": "123 Main St", "emp_salary": 50000},
    {"emp_id": 2, "emp_name": "Jane Smith", "emp_phone": "9876543210", "emp_address": "456 Oak Ave", "emp_salary": 60000},
    {"emp_id": 3, "emp_name": "Alice Johnson", "emp_phone": "5551234567", "emp_address": "789 Pine Rd", "emp_salary": 55000},
    {"emp_id": 4, "emp_name": "Bob Brown", "emp_phone": "4449876543", "emp_address": "321 Elm St", "emp_salary": 52000},
    {"emp_id": 5, "emp_name": "Emma Davis", "emp_phone": "6665551234", "emp_address": "654 Birch Ln", "emp_salary": 58000},
]

# Define the CSV file path
csv_file_path = "employee_data.csv"

# Write the data to a CSV file
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["emp_id", "emp_name", "emp_phone", "emp_address", "emp_salary"])
    writer.writeheader()  # Write the header row
    for row in data:
        writer.writerow(row)

print(f"CSV file '{csv_file_path}' has been created successfully!")
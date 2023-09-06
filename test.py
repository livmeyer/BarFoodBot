import csv

# Initialize an empty list to store the integer values
data = []

# Open the CSV file for reading
with open('LED_Patterns/idle/phase1.csv', mode='r') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        # Convert each item in the row to an integer and append it to the list
        int_row = [row]
        data.append(int_row)

# Now, 'data' is a list of lists containing the integer values from the CSV file
print(data)

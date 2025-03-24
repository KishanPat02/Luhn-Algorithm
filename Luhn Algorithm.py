Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Names: Kishan Patel, Ibrahim Hussain
... # Assignment Name: Luhn Assignment
... # Due Date: Friday, November 29th
... 
... # How It Works
... '''
... The user is presented with a menu to either enter customer information or generate a customer data file.
... When entering customer information, the user will be prompted for personal details, and validation checks will ensure correct postal code and credit card format.
... When generating the customer data file, the program will output a CSV file with all the customer data entered so far.
... '''
... 
... import csv  # Imports the CSV module for working with files
... 
... POSTAL_CODES_FILE = "postal_codes.csv"  # File path for valid postal codes
... CUSTOMER_ID = 1  # Initial ID for the customer
... 
... # Prints the main menu options for the user
... def printMenu():
...     print('''
...           Customer and Sales System\n
...           1. Enter Customer Information\n
...           2. Generate Customer data file\n
...           3. Report on total Sales (Not done in this part)\n
...           4. Check for fraud in sales data (Not done in this part)\n
...           9. Quit\n
...           Enter menu option (1-9)
...           ''')
... 
... # Allows the user to input customer data with validation checks
... def enterCustomerInfo():
...     global CUSTOMER_ID  # Access and modify the global CUSTOMER_ID variable
... 
...     first_name = input("Enter first name: ")  # Ask for the customer's first name
    last_name = input("Enter last name: ")  # Ask for the customer's last name
    city = input("Enter city: ")  # Ask for the city of the customer

    # Validate the postal code
    postal_code = input("Enter postal code: ")
    while not validatePostalCode(postal_code):  # Repeat until a valid postal code is provided
        print("Invalid postal code. Please try again.")
        postal_code = input("Enter postal code: ")

    # Validate the credit card number
    credit_card = input("Enter credit card number: ")
    while not validateCreditCard(credit_card):  # Repeat until a valid credit card is provided
        print("Invalid credit card number. Please try again.")
        credit_card = input("Enter credit card number: ")

    # Store the customer details in a dictionary
    customer = {
        "id": CUSTOMER_ID,  # Assign the current customer ID
        "first_name": first_name,  # Store the first name
        "last_name": last_name,  # Store the last name
        "city": city,  # Store the city
        "postal_code": postal_code,  # Store the postal code
        "credit_card": credit_card  # Store the credit card number
    }

    CUSTOMER_ID += 1  # Increment the global CUSTOMER_ID for the next customer

    print(f"Customer {first_name} {last_name} added with ID {customer['id']}.")  # Confirm the addition
    return customer  # Return the customer details

# Checks if a postal code is valid by comparing it with a list from a file
def validatePostalCode(postal_code):
    with open(POSTAL_CODES_FILE, 'r') as file:  # Open the postal codes file
        reader = csv.reader(file, delimiter='|')  # Read the file's content with a delimiter
        valid_postal_codes = [row[0] for row in reader]  # Extract valid postal codes from the file
        return postal_code[:3] in valid_postal_codes  # Check if the first 3 characters match

# Validates a credit card number using the Luhn algorithm
def validateCreditCard(card_number):
    reversed_digits = card_number[::-1]  # Reverse the credit card number for processing
    sum1 = 0  # Sum of digits at odd positions
    sum2 = 0  # Sum of processed digits at even positions

    for i in range(len(reversed_digits)):  # Iterate through the reversed digits
        digit = int(reversed_digits[i])  # Convert the character to an integer

        if i % 2 == 0:  # If the digit is in an odd position
            sum1 += digit  # Add it to sum1
        else:  # If the digit is in an even position
            doubled = digit * 2  # Multiply the digit by 2
            if doubled > 9:  # If the result is greater than 9
                sum2 += (doubled - 9)  # Add the sum of the digits
            else:
                sum2 += doubled  # Otherwise, add the doubled value directly

    total = sum1 + sum2  # Calculate the total sum
    return total % 10 == 0  # Valid if the total ends in 0

# Generates a CSV file containing all the customer data
def generateCustomerDataFile(customers):
    file_name = input("Enter the output file name (e.g., customers.csv): ")  # Ask for a file name
    with open(file_name, 'w', newline='') as file:  # Open the file for writing
        writer = csv.writer(file)  # Create a CSV writer object
        writer.writerow(["Customer ID", "First Name", "Last Name", "City", "Postal Code", "Credit Card"])  # Write header
        for customer in customers:  # Write each customer's data
            writer.writerow([customer["id"], customer["first_name"], customer["last_name"], 
                             customer["city"], customer["postal_code"], customer["credit_card"]])
    print(f"Customer data saved to {file_name}.")  # Confirm that the file has been saved

####################################################################

# Main Program
userInput = ""  # Initialize the user input variable
enterCustomerOption = "1"  # Option to enter customer information
generateCustomerOption = "2"  # Option to generate a customer data file
exitCondition = "9"  # Option to quit the program

customers = []  # List to store all customer data

while userInput != exitCondition:  # Continue until the user chooses to quit
    printMenu()  # Display the menu
    userInput = input()  # Get the user's menu selection

    if userInput == enterCustomerOption:  # If the user selects to enter customer information
        customer = enterCustomerInfo()  # Call the function to gather customer details
        customers.append(customer)  # Add the customer to the list

    elif userInput == generateCustomerOption:  # If the user selects to generate the data file
        if customers:  # Check if there are customers to save
            generateCustomerDataFile(customers)  # Generate the file
        else:
            print("No customers have been added yet.")  # Notify if no customers exist

    else:
        print("Please type in a valid option (A number from 1-9)")  # Handle invalid menu input

print("Program Terminated")  # Print a message when the program ends

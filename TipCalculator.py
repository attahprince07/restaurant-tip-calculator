# Tip calculator program
print("Welcome to the tip calculator.\n")

# Collect inputs and convert them to appropriate types
total_bill = float(input("What was the total bill? "))
number_of_people = int(input("How many people to split the bill? "))
tip_percent = int(input("What percentage of tip would you like to give? 10, 12, or 15? "))

# Calculate bill per person
bill_per_person = (total_bill * (1 + (tip_percent / 100))) / number_of_people

# Additional logic for specific tip percentages
if tip_percent == 10:
    bill_per_person = (total_bill * (1 + (10 / 100))) / number_of_people
    print(f"Each person should pay: ${bill_per_person:.2f}")
elif tip_percent == 12:
    bill_per_person = (total_bill * (1 + (12 / 100))) / number_of_people
    print(f"Each person should pay: ${bill_per_person:.2f}")
elif tip_percent == 15:
    bill_per_person = (total_bill * (1 + (15 / 100))) / number_of_people
    print(f"Each person should pay: ${bill_per_person:.2f}")
else:
    print("Invalid tip percentage. Please choose 10, 12, or 15.")


"""Author: Asaia Palacios. Name of program: Taxes and tip calculator. What it does: A program in Python that will help you know, from a meal's price before tax, how much you'll pay, taxes and tips included."""

print "Welcome to the taxes and tip calculator!"

# Prompts for user input
# Use float function to convert input statement string to a real number or "float" in python
meal = float(input("What is the price before tax?"))
tax = float(input("What are the taxes? (in %)"))
tip = float(input("What do you want to tip? (in %)"))

# Calculation to determine: price of meal after tax and total price when factoring tip 
total = (meal+(meal*tax/100))*(1+(tip/100))

# Include price with exactly 6 numbers after the decimal
print("The price you need to pay is: $ %.6f.")% total



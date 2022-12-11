# This program generates a random credit card number

# Import the random module
import random

# Define a function to generate the credit card number
def generate_credit_card_number(bin):
  # Generate a random number that starts with the given BIN
  number = bin
  for i in range(12):
    number += str(random.randint(0, 9))

  # Calculate the checksum using the Luhn algorithm
  checksum = 0
  for i in range(15, -1, -2):
    checksum += int(number[i])
  for i in range(14, -1, -2):
    digit = int(number[i]) * 2
    if digit > 9:
      digit -= 9
    checksum += digit

  # Add the checksum to the number and return it
  return number + str((10 - checksum % 10) % 10)

# Define a function to generate the expiration date
def generate_expiration_date():
  # Generate a random expiration date
  year = str(random.randint(2022, 2031))
  month = str(random.randint(1, 12)).zfill(2)
  return month + "/" + year

# Define a function to generate the CVV
def generate_cvv():
  # Generate a random 3-digit CVV
  return str(random.randint(100, 999))

# Generate and print the credit card number, expiration date, and CVV
credit_card_number = generate_credit_card_number("4111")
expiration_date = generate_expiration_date()
cvv = generate_cvv()

print("Credit card number:", credit_card_number)
print("Expiration date:", expiration_date)
print("CVV:", cvv)

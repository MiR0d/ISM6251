# Variable definitions:
# a = Name of the associate
# n = Name of the business
# b = Monthly advertising budget
# s = Digital Advertising Setup Fee
# f = Monthly management fee
# tar = Total annual revenue
# c = Commission

# Request for information
print("Sales and Sales Associate Commission Tracker by Michael Rodriguez")
a = input("Enter the name of the sales associate: ")
n = input("What is the name of the business for this contract? ")
b = float(input("What is the monthly advertising budget (b)? "))
s = float(input("What is the agreed Digital Advertising Setup Fee? "))

# Variables and Calculations
fixed_fee = 2500
monthly_percentage = 0.15
commission_percentage = 0.05
f = fixed_fee + monthly_percentage * b
tar = s + 12 * f
c = tar * commission_percentage


# Formatting
b = '{0:.2f}'.format(b)
s = '{0:.2f}'.format(s)
f = '{0:.2f}'.format(f)
tar = '{0:.2f}'.format(tar)
c = '{0:.2f}'.format(c)

# Spacing
print()
print()
print()

# Final print out
print("Given b = $", b, ", s = $", s, " for ", n, ".", sep="")
print("Your monthly management fee will be $", f, ".", sep="")
print("The total revenue from this sale will be $", tar, " and the commission earned by ", a, " will be $", c, ".", sep="")
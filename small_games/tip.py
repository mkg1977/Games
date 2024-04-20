print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill?\n"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

total_bill = bill + (bill*tip/100)
pay_per_person = round(total_bill / people, 2)
final_amount = "{:.2f}".format(pay_per_person)


print(f"Each person should pay: ${final_amount}")
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 


print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("How much tip would you like to give? 15, 20 or 25 "))

people = int(input("How many people are splitting the bill? "))

tip_as_pct = tip / 100

total_tip = bill * tip_as_pct

total_bill = bill + total_tip

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay {final_amount}")




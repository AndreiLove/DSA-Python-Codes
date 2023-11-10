print("Welcome to the Trip Cost Calculator!")
days = int(input("How many days will you stay? "))
hotel = float(input("How much does hotel cost pre night? "))
flight = float(input("How much does flight cost? "))
car = float(input("Renatl car cost? "))
other = float(input("Enter other possible expenses: "))

total = round(days+hotel+flight+car+other,2)

print(f"Total Cost: ${total}")
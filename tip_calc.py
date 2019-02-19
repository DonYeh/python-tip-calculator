total_bill = float(input('Total bill amount? '))
service_level = input('Level of service? ')
if service_level == "good":
    tip_amount = .20 * total_bill
elif service_level == "fair":
    tip_amount = .15 * total_bill
elif service_level == "bad":
    tip_amount = .10 * total_bill

total_amount = total_bill + tip_amount

print(('Tip amount: $%.2f') % float(tip_amount))
print(('Total amount: $%.2f') % float(total_amount))

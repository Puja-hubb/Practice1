customer_name = input()
age = int(input())
number_of_tickets = int(input())

if age < 12:
    ticket_price = 120
elif age <= 59:
    ticket_price = 200
else:
    ticket_price = 150

total_before_discount = ticket_price * number_of_tickets

if number_of_tickets >= 5:
    discount = total_before_discount * 10 // 100
else:
    discount = 0

final_amount = total_before_discount - discount

print("Customer Name:", customer_name)
print("Ticket Price:", ticket_price)
print("Number of Tickets:", number_of_tickets)
print("Total Before Discount:", total_before_discount)
print("Discount:", discount)
print("Final Amount:", final_amount)
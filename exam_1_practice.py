# Assignment A walkthrough

'''
The City Library calculates late fees for a single book return at the front desk. Every book gets a grace period, but the exact rules depend on who's returning it. A book that's 30 days late or more is treated as lost and carries a flat $15.00 replacement fee, no matter who returns it. A member of the library's Reading Rewards program gets any fee completely waived if their book is less than 7 days late. For everyone else, a book less than 7 days late costs $0.10 per day, and a book 7 days late or more, but under 30, costs $0.25 per day. The front desk clerk enters the number of days the book is late and whether the patron is a Reading Rewards member, and the program tells the patron their fine.

For example, a Reading Rewards member returning a book 3 days late should see this:

Fine: $0.00

A non-member returning a book 10 days late should see this:

Fine: $2.50

Note: this program does not need a loop. It handles one book, once, and stops. Test it by running it several times with different inputs (a member under 7 days, a non-member under 7 days, anyone at 30+ days) to make sure all the cases come out right, not just the two shown above.
'''
'''
days_lost_threshold = 30
days_grace_period = 7
lost_book_fee = 15.00
grace_rate = 0.10
standard_rate = 0.25

days_late = int(input('Enter days late: '))
member_input = input('Is the patron a Reading Rewards member? (yes/no): ')
is_member = member_input == 'yes'

if days_late >= days_lost_threshold:
    fine = lost_book_fee
elif is_member and days_late < days_grace_period:
    fine = 0.00
elif days_late >= days_grace_period:
    fine = float(standard_rate * days_late)
else:
    fine = float(days_late * grace_rate)

print(f'Fine: ${fine:.2f}')
'''



'''
Assignment B: Farmers Market Stand
Focus: Loops and Iteration combined with Selection 

Ridgeline Farmers Market has one stand selling fresh apples by the pound, weighed and priced at checkout. Buying in bulk saves money: orders under 5 pounds are charged $2.50 per pound, orders of 5 pounds up to 15 pounds are charged $2.00 per pound, and orders of 15 pounds or more are charged $1.75 per pound. The vendor keys in each customer's weight in pounds as they check out, one at a time, all through market day. Once there are no more customers, the vendor presses Enter with nothing typed, and the program needs to report how many customers bought apples, the total pounds sold, the total money collected, and the single largest amount any one customer paid, all by the end of market day.

For example, if one customer buys 3 pounds, a second buys 10 pounds, and a third buys 20 pounds, the program should produce exactly this:

Customers served: 3
Total pounds sold: 33.0
Total revenue: $62.50
Largest single payment: $35.00
'''

# weights
low_tier_max = 5
mid_tier_max = 15
# price based on weight
low_price = 2.50
mid_price = 2.00
high_price = 1.75

customer_count = 0
total_pounds = 0.0
total_revenue = 0.0
largest_payment = 0.0

weight_input = input('Enter pounds purchased (or press Enter to end): ')
while weight_input != "":
    weight = float(weight_input)
    if weight >= mid_tier_max:
        price = high_price
    elif weight >= low_tier_max:
        price = mid_price
    else:
        price = low_price
    paid = weight * price
    if paid > largest_payment:
        largest_payment = paid
    total_pounds += weight
    total_revenue += paid
    customer_count += 1
    weight_input = input('Enter pounds purchased (or press Enter to end): ')

print(f'Customers served: {customer_count}')
print(f'Total pounds sold: {total_pounds}')
print(f'Total revenue: ${total_revenue:.2f}')
print(f'Largest single payment: ${largest_payment:.2f}') 
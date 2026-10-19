"""
CIS 3680 - Week 3: Operators, Expressions, and Type Conversion
Streaming Subscription Calculator - In-Class Practice

This is practice only. Nothing in this file is submitted or graded.
Fill in each ADD THIS line where marked. Everything else already works.
Covers both Monday and Wednesday's class sessions, in order.
"""

#===== INPUTS =====
netflix = 15.49
hulu = 7.99
spotify = 11.99
disney_plus = 13.99
budget_cap = 75.00
youtube = 10.99
# Prices of all subscriptions, budget_cap is max monthly spending allowed

saving_goal = 500

#===== CALCULATIONS =====
total_monthly = netflix + hulu + spotify + disney_plus + youtube
# add all subscriptions and get total
percent_correct = total_monthly / budget_cap * 100
# calculate how much of the monthly budget is used up by subscription costs
weekly_cost = total_monthly / 4
# same as above but divide into weekly costs
budget_left = budget_cap - total_monthly
# current number of months it will take to save $500
monthly_no_netflix = hulu + spotify + disney_plus + youtube
# monthly cost of subscriptions minus netflix
budget_no_netflix = budget_cap - monthly_no_netflix
# budget left over if you cancel netflix
saving_months = saving_goal / budget_no_netflix
# number of months it will take to save $500 minus netflix


#===== OUTPUTS =====
# show values of calculations from above
print(f"Total montly budget:                     $ {budget_cap:.2f}")
print(f"Total monthly cost:                      $ {total_monthly}")
print(f"Total weekly cost:                       $ {weekly_cost:.2f}")
print(f"Percent of budget used:                    {percent_correct:.1f} %")
print(f"Months to save $500 by cancelling Netflix: {saving_months:.0f}")

# What share of the total bill is Netflix alone?
netflix_share = netflix / total_monthly * 100
print(f"Netflix's share of the bill:               {netflix_share:.1f} %")

# How many whole months of Netflix does $100 buy?
whole_months = int(100 / netflix)
print(f"How many months you can buy with $100:     {whole_months}")

# How can you see the leftover money?
leftover_manual = 100 - whole_months * netflix
print(f"How much money is left from $100:        $ {leftover_manual:.2f}")

# What is the cost of the Netflix?
#whole_months_floor = int(100 // netflix) 
#leftover_mod = 100 % netflix
#print(whole_months_floor)
#print(f"{leftover_mod:.2f}")

print("")

# Disney is raising prices by 8%, what is new total monthly bill?
new_total = total_monthly - disney_plus + (disney_plus * 1.08)
print(f"New total after price increase:          $ {new_total:.2f}")



# ============================================================
# WEDNESDAY - only start this section once everything above already
# runs correctly. Same file, same variables from Monday.
# ============================================================

# ----- PROCESS: Annual cost with a discount (the wrong way, on purpose) -----
# Type this exactly as shown.


discount = 0.10
annual_cost = (netflix + hulu + spotify + disney_plus + youtube) * 12

# ----- PROCESS: Annual cost with a discount (the correct, deliberate way) -----
# ADD THIS: write annual_correct. Group (1 - discount) in parentheses
# before multiplying by total_monthly and 12

annual_correct = total_monthly * 12 * (1 - discount)




# ----- OUTPUT -----
# ADD THIS: print annual_correct as a formatted f-string, labeled
# "Annual cost with discount: $", rounded to 2 decimal places
print(f"Annual cost without discount:            $ {annual_cost:.2f}")
print(f"Annual cost with discount:               $ {annual_correct:.2f}")
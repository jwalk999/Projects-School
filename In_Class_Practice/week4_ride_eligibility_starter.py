"""
CIS 3680 - Week 4: Boolean Logic and Selection Statements
Ride Eligibility Checker - In-Class Practice

This is practice only. Nothing in this file is submitted or graded.
Fill in each ADD THIS line where marked. Everything else already works.
"""

# ----- INPUT (already set up, nothing new here) -----
height = 50
age = 11
accompanied_by_adult = True


# ----- PROCESS: Mistake 1 - elif order bug (the wrong way, on purpose) -----
# Type this exactly as shown. We are about to find out why it's risky.
if height >= 36:
    tier_wrong = "Family"
elif height >= 48:
    tier_wrong = "Thrill"
elif height >= 54:
    tier_wrong = "Extreme"
else:
    tier_wrong = "Kiddie"
print(tier_wrong)

# ADD THIS: as a comment, write down whether "Family" sounds right
# for someone 50 inches tall. Talk to your neighbor before moving on.


# ----- PROCESS: Ride tier (the correct, deliberate way) -----
# ADD THIS: write the same kind of if/elif/else chain as above, but
# check height from LARGEST threshold down to smallest: 54, then 48,
# then 36, else Kiddie. Store the result in a variable called
# tier_correct

if height >= 54:
    tier_correct = "Extreme"
elif height >= 48:
    tier_correct = "Thrill"
elif height >= 36:
    tier_correct = "Family"
else:
    tier_correct = "Kiddie"
print(tier_correct)


# ----- OUTPUT -----
# ADD THIS: print tier_correct as a formatted f-string, labeled
# "Ride tier: "


# ----- PROCESS: Mistake 2 - and/or confusion (the wrong way, on purpose) -----
# A second rider: tall enough for Extreme, but not old enough.
# Type this exactly as shown.
height2 = 56
age2 = 11

extreme_eligible = height2 >= 54 and age2 >= 13
print(f"Cleared for Extreme Coaster: {extreme_eligible}")

# ----- PROCESS: Family Coaster (a correct, working example, not a mistake) -----
# The Family Coaster allows riders 42 inches or taller on their own,
# OR shorter riders down to 36 inches if an adult goes with them.
# ADD THIS: write family_eligible using height3, 42, 36, and
# accompanied_by_adult, grouping the second condition in parentheses
height3 = 38
family_eligible = height3 >= 42 or (height3 >= 36 and accompanied_by_adult)
print(f"Cleared for Family Coaster: {family_eligible}")
# ----- OUTPUT -----
# ADD THIS: print family_eligible as a formatted f-string, labeled
# "Cleared for Family Coaster: "


# ----- GUIDED PRACTICE -----
# ADD THIS: add one more rule to the Ride Eligibility Checker using
# at least one compound condition (and/or) and at least one elif
# branch. Some ideas:
#   - Add a height-and-age combined rule for the Thrill tier.
#   - Add a "Kiddie Plus" tier that requires either a minimum height
#     OR being accompanied by an adult.
#   - Add a maximum age rule for the Kiddie rides.
# Print the result clearly labeled.

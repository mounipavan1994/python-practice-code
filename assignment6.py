'''A shop offers a discount when a customer's bill is at least ₹1,000 and the customer has a membership.

Requirements

Ask for the bill amount and membership status.

Use comparison operators to check eligibility.

Use logical operators such as and, or and not.

Print whether the customer is eligible for a discount.

Challenge: Add a second rule: a special coupon can qualify a non-member for the discount too.'''

x=int(input('Bill Amount:' ))
y=input('Tell me membership: ')

if x==1000 and y=="yes":
    print('Eligible')
else:
    print('Not eligible')

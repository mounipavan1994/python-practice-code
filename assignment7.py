'''Ask the user to enter marks out of 100.

Use if, elif and else to display a grade:

Marks

	

Grade




90–100

	

A




75–89

	

B




60–74

	

C




35–59

	

D




Below 35

	

Fail

Requirements

Reject marks below 0 or above 100.

Display the appropriate grade.

Test boundary values such as 35, 60, 75 and 90.'''



x=int(input('enter the markk: '))
print(type(x))
if x>=90 and x<=100:
    print('grade A')
elif x>=75 and x<=89:
    print('grade B')
elif x>=60 and x<=74:
    print('grade C')
elif x>=35 and x<=59:
    print('grade D')
else:
    print('fail')

    mounipavan@94 -> Password
    mounipavan1994 -> username
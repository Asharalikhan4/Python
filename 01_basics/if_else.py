age = 10

if age > 11:
    print('Age is greter then 10')
elif age < 11:
    print('Age is less then 10')
else :
    print(f'Age is {age}')


'''
-> Advance Syntax/ Inline Conditionals/ Ternary Operator
'''

status = "Access Granted" if age > 10 else "Access Denied"
print(status)
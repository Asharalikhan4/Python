'''
-> In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.
-> There are two types of type conversion in Python.
1. Implicit Conversion - automatic type conversion
2. Explicit Conversion - manual type conversion
-> Python always converts smaller data types to larger data types to avoid the loss of data. (Implicit)
-> In Type Casting (Explicit), loss of data may occur as we enforce the object to a specific data type.
'''

integer_number = 10
float_number = 10.10

new_number = integer_number + float_number
print(new_number, type(new_number))

num_string = '10'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))
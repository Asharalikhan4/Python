'''
-> In Python, exceptions are runtime errors. Exception handling is the process of writing "contingency plans" so your program can gracefully recover from unexpected events (like a missing file, a downed network, or a user typing a letter instead of a number) rather than crashing outright.
-> Python uses four core block to handle the exceptions gracefully:
    1. try, test a block of code for errors, Always runs first.
    2. except, Handles the error gracefully, Only if an exception occurs in the try block.
    3. else, Runs code that depends on the try block succeeding, Only if no exception occurs.
    4. finally, Executes cleanup tasks (Closing files), Always regardless of success of failure.
'''

def read_and_divide(file_path):
    try:
        file = open(file_path, "r")
        data = int(file.read())
        result = 100/data

    except FileNotFoundError:
        print("Error: The file was not found.")

    except (ValueError, TypeError) as e:
        print(f"Error: The file contains invalid data. Details: {e}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print(f"Success! The result is {result}")

    finally:
        print("Closing the file...")
        if 'file' in locals() and not file.closed:
            file.close()


'''
-> You can define your own exceptions by inheriting from python's built-in Exception class. This is highly recommended in professional codebases to make errors domain-specific and descriptive.
'''

class InsuffcientFundsError(Exception):
    '''Custom exception for invalid banking operations...'''
    pass

def withdraw(balance, amount):
    if amount > balance:
        # Manually triggering the Exception
        raise InsuffcientFundsError(f"Cannot withdraw {amount}. Balance is only {balance}")
    return balance - amount
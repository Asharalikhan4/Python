'''
1. If a try block has a return statement, and the finally block also has a return statement, which value does the function actually return?
-> The function returns the value from the finally block. Because the finally block is guaranteed to execute right before the function exits, its return statement silently overrides any return executed in the try, except, or else blocks.
'''


'''
2. Why is writing a bare except: considered bad practice in production code?
-> A bare except: catches everything, including system-level interrupts like KeyboardInterrupt (when a user presses Ctrl+C to kill the script) or SystemExit. This can make a hanging program impossible to shut down gracefully and often masks hidden bugs. You should always catch the specific exceptions you anticipate (like KeyError or ConnectionError).
'''


'''
3. You catch a database error, but you want to raise a custom application error without losing the original database traceback. How do you do this?
-> You use the raise ... from ... syntax to chain them together.
try:
    1 / 0
except ZeroDivisionError as e:
    raise ValueError("Invalid mathematical operation") from e
This preserves both tracebacks, showing the developer: "The above exception was the direct cause of the following exception."
'''


'''
4. Why use the else block? Why not just put the success code at the bottom of the try block?
-> Keeping the try block as small as possible is a major best practice. If you put success code inside the try block, you risk catching an exception raised by that success code, which makes debugging highly confusing. The else block strictly isolates code that should only run if the risky operation succeeded, without mistakenly catching its subsequent errors.
'''


# Output Based Question
# 5
def process_data():
    try:
        print("A", end="")
        raise ValueError()
    except ValueError:
        print("B", end="")
        return "Done"
    finally:
        print("C", end="")

process_data()


# 6
def calculate_value():
    try:
        result = 10/2
    except ZeroDivisionError:
        result = 0
    else:
        result += 5
    finally:
        result += 2
    return result

calculate_value()

# 7, In python, KeyError is a subclass of LookupError
try:
    my_dict = {'a': 1}
    print(my_dict['b'])
except LookupError:
    print("LookupError caught")
except KeyError:
    print("KeyError caught")

# Read about asyncio.gather, TaskGroups and except*(Python 3.11+)
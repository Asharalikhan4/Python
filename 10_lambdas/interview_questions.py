'''
1. What is the output of the following code
'''

funcs = [lambda: i for i in range(3)]
result = [f() for f in funcs]
print("result", result)
# Output: [2, 2, 2]
'''
-> The Explanation: Lambdas do not evaluate their internal expressions when they are created; they evaluate them when they are called. By the time the second list comprehension actually calls the functions, the first for loop has finished, and the variable i is sitting at its final value of 2. All three lambdas look up i and see 2
'''


'''
How would you fix it so it outputs [0, 1, 2]
'''
new_funcs = [lambda i=i: i for i in range(3)]
new_result = [f() for f in new_funcs]
print("new_result", new_result)


'''
2. You have a list of employee dictionaries. How would you use sorted() and a lambda to sort them first by score (descending), and then by name (ascending/alphabetical)?
'''
employees = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 90},
    {"name": "Charlie", "score": 85}
]
sorted_emps = sorted(employees, key=lambda e: (-e["score"], e["name"]))
'''
-> The Explanation: When a lambda returns a tuple, Python sorts by the first item in the tuple. If there is a tie, it looks at the second item. Because we cannot pass reverse=True (as that would reverse the names too), we use a math trick: putting a minus sign (-) in front of the integer forces the scores to sort in descending order, while the strings sort normally.
'''


'''
3. Can you put a try/except block, a while loop, or a variable assignment (like x = 5) inside a lambda function? Why or why not?
-> The Answer: No, you cannot.

The Explanation: Python strictly dictates that lambdas can only contain expressions (things that evaluate to a value, like x + 5 or x > 10), not statements (things that perform an action, like try, return, pass, or x = 5).

If you absolutely need conditional logic inside a lambda, you must use an inline if/else expression (e.g., lambda x: "Even" if x % 2 == 0 else "Odd"). If you need error handling or loops, you must abandon the lambda and write a standard def function.
'''

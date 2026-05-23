'''
1. What are some real world use case of iterator?
-> Processing Massive Log files and CSV's
-> Database Cursors and API Pagination
-> Infinite Data Streams
'''


'''
2. What will be the output of this code and why?
'''
my_list = [1, 2, 3]
my_iterator = iter(my_list)

# Loop 1
print("First pass:")
for num in my_iterator:
    print(num)

# Loop 2
print("Second pass:")
for num in my_iterator:
    print(num)
'''
-> The first loop prints 1, 2, 3. The second loop prints absolutely nothing.
The Explanation: Iterators are one-way streets. Once you call next() and consume an item, it is gone from the iterator. When the first loop finishes, the iterator is "exhausted" (empty). To loop through the data again, you must create a brand new iterator by calling iter(my_list) again.
'''


'''
3. You have a machine with 8GB of RAM. I give you a 100GB text file containing numbers. How do you find the sum of all the numbers in Python without crashing the machine?
-> You use an iterator (specifically, a generator expression) to read and sum the file line-by-line.
Because the built-in sum() function accepts an iterator, you can pass a generator directly into it. It will stream the numbers one by one, keeping a running total, and memory usage will remain near zero.
'''
# The memory-safe solution
with open('numbers.txt') as f:
    total = sum(int(line.strip()) for line in f)


'''
4. If I want to build a custom class that works in a for loop, what two dunder methods must I implement, and what is the specific job of each?
-> You must implement the Iterator Protocol, which requires __iter__ and __next__:
    __iter__(): Its only job is to return the iterator object itself (usually by returning self). It sets up the starting state.
    __next__(): Its job is to return the very next piece of data. When there is no more data to give, it is legally required by Python to raise a StopIteration exception, which is the secret signal that tells a for loop to terminate.
'''
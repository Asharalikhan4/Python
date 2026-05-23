'''
-> A iterator is an object that allows you to traverse through all the values in a collection (like a list or string) exactly one at a time.
-> To understand iterators, it helps to use a real-world analogy: a book and a bookmark.
Imagine a list in Python is like a physical book. The book holds all the pages, but the book itself doesn't know what page you are currently reading. To keep track of your place, you use a bookmark.
In Python, the list is the Iterable (the book), and the Iterator is the bookmark. It is a special object that remembers exactly where you are in a sequence of data and knows how to fetch the very next item.

-> The Iterator Protocol
For an object to officially be an "iterator" in Python, it must follow the Iterator Protocol. This means the object's class must contain two specific magic (dunder) methods:
    __iter__(): This initializes the iterator and returns the iterator object itself.
    __next__(): This fetches the next value in the sequence. When there is no more data left, it must raise a special exception called StopIteration.

-> Iterable vs. Iterator
This is the biggest point of confusion for Python learners.
Iterable (The Book): Things like Lists, Strings, Tuples, and Dictionaries. You can loop over them, but they are not iterators themselves.
Iterator (The Bookmark): The engine that actually powers the loop.
To turn an iterable into an iterator, you use the built-in iter() function. Then, you use next() to move forward.
'''

my_list = ["Apple", "Banana", "Cherry"]

# my_list is an Iterable. We create an Iterator from it.
my_iterator = iter(my_list)

# Now we manually ask for the next item
print(next(my_iterator))  # Outputs: Apple
print(next(my_iterator))  # Outputs: Banana
print(next(my_iterator))  # Outputs: Cherry

# If we call it again, there is no more data!
print(next(my_iterator))  # ❌ Crashes with: StopIteration exception

'''
Building a custom iterator
'''
class Counter:
    def __init__(self, max_limit):
        self.current = 0
        self.max_limit = max_limit
        
    def __iter__(self):
        # Returns the iterator object itself
        return self
        
    def __next__(self):
        self.current += 1
        
        # Check if we hit the limit
        if self.current > self.max_limit:
            raise StopIteration
            
        return self.current

# Using our custom iterator in a normal for-loop!
my_counter = Counter(3)

for number in my_counter:
    print(number)
    
# Output:
# 1
# 2
# 3
# Numeric Types
# Integer: a whole number without a fractional part.
x = 10
y = -5
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'int'>

# Float: a number that has a decimal point.
a = 10.5
b = -3.4
print(type(a))  # Output: <class 'float'>
print(type(b))  # Output: <class 'float'>

# Complex: a number with a real and an imaginary part.
c = 2 + 3j
d = 4 - 2j
print(type(c))  # Output: <class 'complex'>
print(type(d))  # Output: <class 'complex'>

# Sequence Types
# String: a sequence of characters.
name = "Alice"
greeting = 'Hello, World!'
print(type(name))  # Output: <class 'str'>
print(type(greeting))  # Output: <class 'str'>

# List: ordered and mutable collection of items.
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
print(type(fruits))  # Output: <class 'list'>
print(type(numbers))  # Output: <class 'list'>

# Tuple: ordered and immutable collection of items.
point = (3, 4)
colors = ("red", "green", "blue")
print(type(point))  # Output: <class 'tuple'>
print(type(colors))  # Output: <class 'tuple'>

# Mapping Type
# Dictionary: unordered collection of key-value pairs.
student = {"name": "John", "age": 20, "courses": ["Math", "Science"]}
print(type(student))  # Output: <class 'dict'>

# Set Types
# Set: unordered collection of unique items.
fruits_set = {"apple", "banana", "cherry"}
print(type(fruits_set))  # Output: <class 'set'>

# Frozenset: immutable version of a set.
vowels = frozenset({"a", "e", "i", "o", "u"})
print(type(vowels))  # Output: <class 'frozenset'>

# Boolean Type
# Boolean: represents True or False.
is_active = True
is_deleted = False
print(type(is_active))  # Output: <class 'bool'>
print(type(is_deleted))  # Output: <class 'bool'>

# None Type
# NoneType: represents the absence of a value.
result = None
print(type(result))  # Output: <class 'NoneType'>

# Advanced Data Types
# Bytes: immutable sequence of bytes.
data_bytes = b"Hello"
print(type(data_bytes))  # Output: <class 'bytes'>

# Bytearray: mutable sequence of bytes.
data_bytearray = bytearray(b"Hello")
data_bytearray[0] = 72  # Modify the first byte
print(data_bytearray)  # Output: bytearray(b'Hello')
print(type(data_bytearray))  # Output: <class 'bytearray'>

# Memoryview: allows access to the internal data of an object that supports the buffer protocol without copying.
data = bytearray('XYZ', 'utf-8')
mem_view = memoryview(data)
print(mem_view[0])  # Output: 88 (ASCII value of 'X')
print(type(mem_view))  # Output: <class 'memoryview'>

# Custom Data Types
# Class and Object: user-defined types created using classes.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person = Person("Alice", 30)
print(person.greet())  # Output: Hello, my name is Alice and I am 30 years old.
print(type(person))  # Output: <class '__main__.Person'>

# 🐍 Python for Machine Learning Cheatsheet

## Data Types & Structures
```python
# List
my_list = [1, 2, 3, "four"]
my_list.append(5)

# Dictionary
my_dict = {"a": 1, "b": 2}
my_dict["c"] = 3

# Set (unique elements)
my_set = {1, 2, 3, 3} # {1, 2, 3}

# Tuple (immutable)
my_tuple = (1, 2, 3)
```

## String Operations
```python
s = "Hello World"
s.lower()
s.upper()
s.split(" ") # ['Hello', 'World']
f"Format string: {s}"
```

## List Comprehensions
```python
squares = [x**2 for x in range(10) if x % 2 == 0]
```

## Functions & Lambda
```python
def add(a, b=0):
    return a + b

multiply = lambda x, y: x * y
```

## Classes & OOP Basics
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
```

## File I/O
```python
with open("file.txt", "w") as f:
    f.write("Hello")
with open("file.txt", "r") as f:
    content = f.read()
```

## Error Handling
```python
try:
    1 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Always runs")
```

## Iterators & Generators
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1
```

## Decorators
```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")
```

## Type Hints
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Common Standard Library Modules
```python
import os, sys, json, csv
from datetime import datetime
from collections import defaultdict, Counter
import itertools, functools

# JSON
data = json.loads('{"a": 1}')
json_str = json.dumps(data)

# Counter
counts = Counter(['a', 'a', 'b'])
```

## Virtual Environments
```bash
python -m venv myenv
source myenv/bin/activate # Linux/Mac
myenv\Scripts\activate # Windows
```

## Package Management
```bash
pip install numpy
pip freeze > requirements.txt
pip install -r requirements.txt
```

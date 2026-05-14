# DSA-DAY3
````md
# 📅 Day 3 - Python Strings, Dictionaries & Tuples 🚀

Welcome to Day 3 of my DSA with Python learning journey.  
This repository contains Python string methods, dictionary operations, tuple concepts, nested loop patterns, and beginner-level problem-solving programs.

---

# 📌 Topics Covered

## ✅ Python String Methods

Methods Practiced:
- `isalnum()`
- `isalpha()`
- `isdigit()`
- `islower()`
- `isupper()`
- `istitle()`
- `isspace()`
- `startswith()`
- `endswith()`
- `find()`
- `index()`
- `count()`

---

# 📌 String Case Conversion

Functions Used:
- `lower()`
- `upper()`
- `swapcase()`
- `title()`
- `capitalize()`

---

# 📌 String Formatting

Methods Practiced:
- `format()`
- Indexed formatting
- Keyword formatting
- f-strings

Example:
```python
name = "prashant"
sal = 5000
age = 28

print("{} sal is {} age is {}".format(name,sal,age))
print(f"{name} is a good boy")
````

---

# 📌 Nested Loop Pattern Programs

Patterns Practiced:

* Number patterns
* Alphabet patterns
* Star patterns
* Pyramid patterns

Example:

```python
for i in range(1,5):
    for j in range(1,5):
        print(i, end=" ")
    print()
```

---

# 📌 Product of Array Except Self

### Problem

```python
Input : [1,2,3,4]
Output: [24,12,8,6]
```

### Solution

```python
arr = [1,2,3,4]
product = 1

for i in arr:
    product *= i

for i in range(len(arr)):
    arr[i] = product // arr[i]

print(arr)
```

---

# 📌 Dictionary Concepts

Topics Practiced:

* Dictionary creation
* Accessing values using keys
* Updating values
* Looping through keys and values
* `items()`
* `values()`
* `copy()`
* `pop()`

---

# 📌 Dictionary-Based Problems

## ✅ Frequency Count of Elements

### Problem

```python
Input : [1,2,2,3,4,3,5]
Output: {1:1, 2:2, 3:2, 4:1, 5:1}
```

---

## ✅ Maximum & Minimum Values in Dictionary

---

# 📌 String Problem Solving

## ✅ Remove Duplicate Characters

### Problem

```python
Input : "prashant"
Output: "prashnt"
```

---

## ✅ Reverse a String

### Problem

```python
Input : "prashant"
Output: "tnahsarp"
```

---

## ✅ Palindrome Check

### Problem

```python
Input : "NAMAN"
Output: Palindrome
```

---

## ✅ Anagram Check

### Problem

```python
Input : listen, silent
Output: ANAGRAM
```

---

## ✅ Count Vowels & Consonants

---

## ✅ Count Words in Sentence

### Problem

```python
Input : "This is a sentence"
Output: 4
```

---

# 📌 Number Logic Problems

## ✅ Reverse a Number

### Problem

```python
Input : 123456
Output: 654321
```

---

# 📌 Tuple Concepts

Topics Practiced:

* Tuple creation
* Tuple immutability
* Tuple multiplication
* Tuple slicing
* Tuple length operations

---

# 📌 Type Conversion Functions

Functions Practiced:

* `int()`
* `float()`
* `complex()`
* `bool()`

---

# 📌 Concepts Learned

* String manipulation techniques
* Dictionary operations and hashing behavior
* Nested loop logic
* Pattern printing
* Tuple immutability
* Frequency counting
* Problem-solving using loops and conditions

---

# 🛠️ Technologies Used

* Python 3
* VS Code

---

# 🎯 Learning Outcome

Today I practiced Python string methods, dictionaries, tuples, nested loops, and problem-solving programs to improve coding logic and DSA fundamentals.

---

# 🚀 Repository Goal

To document my daily DSA and Python learning journey consistently while improving coding and problem-solving skills.



```
```

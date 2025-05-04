# 🔁 Reverse a Word Using Command-Line Arguments
## This Python script takes a word as a command-line argument, reverses it, and prints the result. It uses the built-in argparse module, making it suitable for automation and scripting tasks.

### 📁 File
##### reverse_args.py

### 🛠️ Requirements
##### Python 3.x

##### No external packages are required — only standard libraries are used.

### 🚀 How to Run

```bash
python reverse_args.py <your_word>
```
##### 📌 Replace <your_word> with the word you want to reverse.

### ✅ Example

```bash
$ python reverse_args.py DevOps
```
spOveD

### 🧠 What This Script Does
##### Uses Python's argparse to accept a word as a command-line argument

##### Reverses the string using slicing: [::-1]

##### Prints the reversed word to the terminal

### 📌 Why Use This?
##### A great first exercise for learning argparse

##### Helps understand slicing in Python

##### Prepares you for automation scripting and DevOps CLI tools

### 📄 Script Content

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("word", type=str, help = "Enter a word to reverse")

args = parser.parse_args()

print(args.word[: :-1])
```

### 📚 Learning Concepts Covered
##### argparse basics

##### Command-line arguments

##### String slicing ([::-1])

##### Python scripting

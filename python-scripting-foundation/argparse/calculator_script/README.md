# 🧮 Calculator Script using argparse
## This Python script performs simple arithmetic operations (addition, subtraction, multiplication, and division) using command-line arguments via the argparse module.

### 📂 File:
##### calc.py

### 🚀 How to Use
##### 📌 Syntax
bash
```
python calc.py --operation OPERATION --x NUMBER1 --y NUMBER2
```

| Argument      | Type   | Description                                      | Required |
|---------------|--------|--------------------------------------------------|----------|
| `--operation` | string | Operation to perform: `add`, `sub`, `mul`, `div` | ✅ Yes   |
| `--x`         | int    | First number                                     | ✅ Yes   |
| `--y`         | int    | Second number                                    | ✅ Yes   |


### ✅ Examples
bash
```
python calc.py --operation add --x 5 --y 3
# Output: 8

python calc.py --operation sub --x 10 --y 4
# Output: 6

python calc.py --operation mul --x 2 --y 6
# Output: 12

python calc.py --operation div --x 8 --y 2
# Output: 4.0
```

### 🧠 What You Learn
##### How to use argparse for command-line argument parsing.

##### Enforcing required inputs and choices.

##### Performing basic math operations based on user input.

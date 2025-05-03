import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--operation', choices=['add', 'sub', 'mul', 'div'], required=True)
parser.add_argument('--x', type=int, required=True)
parser.add_argument('--y', type=int, required=True)

args = parser.parse_args()

x = args.x
y = args.y
op = args.operation

if op == 'add':
    result = x+y
elif op == 'sub':
    result = x-y
elif op == 'mul':
    result = x*y
elif op == 'div':
    result = x/y
else:
    result = "Invalid operation"

print(f'Result: {result}')

import argparse

parser = argparse.ArgumentParser(description = "Search text in a file")

parser.add_argument("--file", type = str, required = True)

parser.add_argument("--search", type = str, required = True)

parser.add_argument("-i", "--ignore-case", action="store_true")

args = parser.parse_args()

try:
    with open (args.file, 'r') as f:
        for line in f:
            if args.ignore_case:
                if args.search.lower() in line.lower():
                    print(line.strip())
            elif args.search in line:
                    print(line.strip())
except FileNotFoundError:
     print("File not found")
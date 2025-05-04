import argparse
import os

parser = argparse.ArgumentParser(description = "Renaming file")

parser.add_argument("old_name", type = str)

parser.add_argument("new_name", type = str)

args = parser.parse_args()

try:
    os.rename(args.old_name, args.new_name)
    print(f"File renamed from {args.old_name} to {args.new_name}")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred: {e}")
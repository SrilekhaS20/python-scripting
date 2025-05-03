import argparse

parser = argparse.ArgumentParser()

parser.add_argument("word", type=str, help = "Enter a word to reverse")

args = parser.parse_args()

print(args.word[: :-1])
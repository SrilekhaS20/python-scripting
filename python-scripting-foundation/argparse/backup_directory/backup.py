import argparse

import os

import shutil

parser = argparse.ArgumentParser(description = "Directory to be backed up in zip format")

parser.add_argument("--source", type=str, required=True)

parser.add_argument("--destination", type=str, required=True)

args = parser.parse_args()

if not os.path.exists(args.source) and not os.path.isdir(args.source):
    print("Source directory is not found")
elif shutil.make_archive(args.destination, "zip", args.source):
    print(f"Backup is successful: {args.destination} is created")
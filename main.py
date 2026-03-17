import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

path = r"C:\Users\sanja\Downloads"

files = os.listdir(path)

for file in files:
    print(file)
import os 

 path = "C:\Users\sanja\Downloads"

 files = os.listdir(path)

 for file in files:
    print(file)
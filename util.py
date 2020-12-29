import time
import os


def saveInFile(msg):
    with open(os.path.join(os.getcwd(), "test.txt"), 'a') as file:
        file.write(msg)
    print(msg)

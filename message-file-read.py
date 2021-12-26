import sys

filename = "message.txt"

try:
  with open(filename, "r") as file:
    print(file.read())
except NameError:
  print("Error: file {}, not found".format(filename))

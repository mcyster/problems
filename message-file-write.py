import sys

filename = "message.txt"

message = input("Enter message to store: ")

try:
  with open(filename, "w") as file:
    file.write(message)
except (FileNotFoundError, IOError, OSError) as e:
  print("Message file {}, not found, trying writing something first".format(filename))

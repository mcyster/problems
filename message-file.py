import sys

filename = "message.txt"
read = False
message = ""

if len(sys.argv) == 1:
  read = True
elif len(sys.argv) == 2:
  message = sys.argv[1]
else:
  print("Usage {} [message]".format(sys.argv[0]))
  sys.exit(1)

if read:
  try:
      with open(filename, "r") as file:
        print(file.read())
  except NameError:
    print("Error: file {}, not found".format(filename))
else:
  try:
      with open(filename, "w") as file:
        file.write(message)
  except IOError:
    print("Error: file {}, not found".format(filename))

import os, sys

thisCommand = os.path.basename(__file__)

files = [file for file in os.listdir(".") if os.path.isfile(file) and file.endswith(".py") and file != thisCommand]


print("Go to the shell tab run, with: python name.py")


print("Programs:")
for index in range(0, len(files)):
  print(index, files[index])

answer = False
while not answer:
  runInput = input("or, enter the number of program to run: ")

  try:
    runIndex = int(runInput)

    if runIndex in range(0, len(files)):
      answer = True
    else:
      print("Please choose a number listed above")
  except ValueError:
    print('Looking for a number')
    runIndex = -1


os.system("python " + files[runIndex])




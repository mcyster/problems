
try:
  value = float(input("Enter a number: "))
except ValueError:
  print("You did not enter a valid number")

if value < 0: 
  print("We don't work with imaginary numbers here!")
  exit(0)

squareRootMin = 0.0
squareRootMax = value

guess = value / 2.0
error = value

while error >= 0.000001:
  guessSquared = guess * guess
  if guessSquared > value:
    squareRootMax = guess
    guess = (guess - squareRootMin) / 2.0 + squareRootMin
  elif guessSquared < value:
    squareRootMin = guess
    guess = (squareRootMax - guess) / 2.0 + guess

  error = abs(value - guessSquared)

print("The square root of {} is {}".format(value, guess))


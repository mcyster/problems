import sys

if len(sys.argv) == 1 or len(sys.argv) > 2:
  print("Usage {} value1/value2".format(sys.argv[0]))
  sys.exit(1)

fraction = sys.argv[1]
fractionParts = fraction.split("/")
if len(fractionParts) == 1:
  inputNumerator = fraction
  inputDenominator = 1
elif len(fractionParts) == 2:
  inputNumerator = fractionParts[0]
  inputDenominator = fractionParts[1]
else:
  print("You did not enter a fraction")
  sys.exit(1)

try:
  numerator = int(inputNumerator)
  denominator = int(inputDenominator)
except ValueError:
  print("You did not enter a valid fraction")

valueWholeNumber = int(numerator / denominator)
numerator = numerator % denominator

for divisor in range(numerator, 1, -1):
  if numerator % divisor == 0 and denominator % divisor == 0:
    numerator = int(numerator / divisor)
    denominator = int(denominator / divisor)
    break
   
print("{}/{} = ".format(inputNumerator,inputDenominator), end = "")
if valueWholeNumber > 0:
  if numerator > 0:
    print("{} {}/{}".format(valueWholeNumber, numerator,denominator))
  else:
    print("{}".format(valueWholeNumber))
else:
  if numerator > 0:
    print("{}/{}".format(numerator,denominator))
  else:
    print("0")

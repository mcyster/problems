

def isPrime(value):
  prime = True
  for divisor in range(2, value):
    if value % divisor == 0:
      prime = False
      break
  return prime

try:
  value = int(input("Enter a number: "))
except ValueError:
  print("You did not enter a valid number")

found = False
for divisor in range(value, 1, -1):
  if isPrime(divisor) and value % divisor == 0:
    found = True
    print("Largest prime factor of {} is {}".format(value, divisor))
    break
   
if not found:
  print("{} has no prime factors".format(value))


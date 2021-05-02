
try:
  value = int(input("Enter a number: "))
except ValueError:
  print("You did not enter a valid number")

isPrime = True
for divisor in range(2, value):
  if value % divisor == 0:
    isPrime = False
    break
   
if isPrime: 
  print("%d is a prime number" % value)
else:
  print("%d is not a prime number" % value)


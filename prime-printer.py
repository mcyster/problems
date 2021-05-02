

primes = []
value = 1
while True:
  isPrime = True
  for divisor in range(2, value):
   if value % divisor == 0:
      isPrime = False
      break
   
  if isPrime: 
    primes.append(value)
    print(value)

  value = value + 1

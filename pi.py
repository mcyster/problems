import random
import math

countInCircle = 0
count = 0

for i in range(1, 5000):
  x = random.uniform(-1,1)
  y = random.uniform(-1,1)

  r = math.sqrt(x * x + y * y)
  if r <= 1:
    countInCircle = countInCircle + 1
  count = count + 1

pi = float(countInCircle) / float(count) * 4
print(pi)

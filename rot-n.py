import sys

# 
# Example usage:
#   echo -e "test1\ntest2" | python rot-n.py 3 | python rot-n.py -3
#

if len(sys.argv) != 2:
  print("Usage {} count".format(sys.argv[0]))
  print("  reads the input stream and 'rotates' the characters by 'count'")
  sys.exit(1)

try:
  count = int(sys.argv[1])
except ValueError:
  print("Count needs to be a number")
  sys.exit(1)

for line in sys.stdin:
  for character in line:
    print(chr(ord(character) + count), end = "")

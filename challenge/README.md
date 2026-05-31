   │ File: 0-fizzbuzz.py
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/python3
   2   │ """ FizzBuzz
   3   │ """
   4   │ import sys
   5   │
   6   │
   7   │ def fizzbuzz(n):
   8   │     """
   9   │     FizzBuzz function prints numbers from 1 to n separated by a space.
  10   │
  11   │     - For multiples of three print "Fizz" instead of the number and for
  12   │       multiples of five print "Buzz".
  13   │     - For numbers which are multiples of both three and five print "FizzBuzz".
  14   │     """
  15   │     if n < 1:
  16   │         return
  17   │
  18   │     tmp_result = []
  19   │     for i in range(1, n + 1):
  20   │         if (i % 3) == 0 and (i % 5) == 0:
  21   │             tmp_result.append("FizzBuzz")
  22   │         elif (i % 3) == 0:
  23   │             tmp_result.append("Fizz")
  24   │         elif (i % 5) == 0:
  25   │             tmp_result.append("Buzz")
  26   │         else:
  27   │             tmp_result.append(str(i))
  28   │     print(" ".join(tmp_result))
  29   │
  30   │
  31   │ if __name__ == '__main__':
  32   │     if len(sys.argv) <= 1:
  33   │         print("Missing number")
  34   │         print("Usage: ./0-fizzbuzz.py <number>")
  35   │         print("Example: ./0-fizzbuzz.py 89")
  36   │         sys.exit(1)
  37   │
  38   │     number = int(sys.argv[1])
  39   │     fizzbuzz(number)
───────┴──────────────────────────────────────────────────────────────────────────────────────────────
───────┬──────────────────────────────────────────────────────────────────────────────────────────────
       │ File: 1-print_square.js
───────┼──────────────────────────────────────────────────────────────────────────────────────────────
   1   │ #!/usr/bin/node
   2   │ /*
   3   │     Print a square with the character #

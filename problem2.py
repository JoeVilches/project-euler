"""
https://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""

# O(n) time, O(1) space
def solution_1(cap):
  previous_fib_term = 1
  current_fib_term = 2
  sum = 0
  while current_fib_term < cap:
    if current_fib_term % 2 == 0:
      sum += current_fib_term

    next_fib_term = previous_fib_term + current_fib_term
    previous_fib_term = current_fib_term
    current_fib_term = next_fib_term

  print(sum)

solution_1(4000000) # 4613732

import math
"""
a lot of math went into a closed form solution, too much for me to comment. But
it works!
"""
# O(1) time, O(1) space
def solution_2(cap):
  root5 = math.sqrt(5)
  a = 2 + root5
  b = 2 - root5
  phi = (1 + root5) / 2
  n = math.floor((math.floor(math.log(root5 * (cap + 0.5), phi)) + 1) / 3)
  solution = root5 * (a*(1-b)*(1-pow(a, n)) - b*(1-a)*(1-math.pow(b, n)))
  print(solution / -20)

solution_2(4000000) # 4613732.0

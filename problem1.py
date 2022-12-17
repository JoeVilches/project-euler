"""
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

# O(n) time, O(1) space
def solution_1():
  sum = 0
  for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
      sum += n

  print(sum)

solution_1() # 233168

"""
sum all the multiples of 3, all the multiples of 5 and add them together. we
double count multiples of 3*5 = 15 so subtract 1 set of those
"""
# O(1) time and space
def solution_2():
  number_of_multiples_of_three = 1000 / 3
  number_of_multiples_of_five = 1000 / 5 - 1 # minus one since 1000 % 5 = 0
  number_of_multiples_of_fifteen = 1000 / 15

  sum_of_multiples_of_three = 3 * (number_of_multiples_of_three * (number_of_multiples_of_three + 1)) / 2
  sum_of_multiples_of_five = 5 * (number_of_multiples_of_five * (number_of_multiples_of_five + 1)) / 2
  sum_of_multiples_of_fifteen = 15 * (number_of_multiples_of_fifteen * (number_of_multiples_of_fifteen + 1)) / 2

  print(sum_of_multiples_of_three + sum_off_multiples_of_five - sum_of_multiples_of_fifteen)

solution_2() # 233168

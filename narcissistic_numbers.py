# 115132219018763992565095597973971522401, aka: Narcissistic Numbers
# 
# 115132219018763992565095597973971522401
# December 14, 2012
# Today we have an exercise, a solution, and a question I don’t know the answer to. The exercise is to write a program that lists the narcissistic numbers in 
# which the sum of the nth powers of the digits of an n-digit number is equal to the number. For instance, 153 is a narcissistic number of length 3 because 
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153. 
# 
# The largest decimal narcissistic number is the 39-digit number that is the title of today’s exercise.

# isNarcissistic :: Int -> Bool
def isNarcissistic(n):
  nstr = str(n)
  l = len(nstr)
  summation = 0
  for x in nstr:
    x = pow(int(x), l)
    summation = summation + x
  if summation == n:
    return True
  else:
    return False
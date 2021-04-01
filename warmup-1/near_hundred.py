def near_hundred(n):
    """ Given an int n, return True if it is within 10 of 100 or 200. 
    Note: abs(num) computes the absolute value of a number. """
    diff1 = abs(n - 100)
    diff2 = abs(n - 200)
    if diff1 <= 10 or diff2 <= 10:
        return True
    return False

print(near_hundred(93)) # True
print(near_hundred(90)) # True
print(near_hundred(89)) # False

# Better way:

def near_hundred(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

print(near_hundred(93)) # True
print(near_hundred(90)) # True
print(near_hundred(89)) # False
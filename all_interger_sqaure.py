# Task
# The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n, print i(square).

# The list of non-negative integers that are less than n=3 is [0,1,2] . Print the square of each number on a separate line.

# Example
# n=3

# Output
# 0
# 1
# 4

n = int(input())

i=0
while i<n:
    print(i**2)
    i+=1 


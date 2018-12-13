"""
Allan Katongole
13th December 2018
Numbers Divisible by 7
and not a multiple of 5
-----------------------
DEV NOTES
-----------------------
1. Use of the range method
"""

numbers = [num for num in range(2000, 3200) if num%7==0 and num%5==0]
print(*numbers, sep=', ')




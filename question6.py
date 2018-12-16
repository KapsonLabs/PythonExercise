"""
Allan Katongole
13 December 2018
Square numbers inbetween
1 and 20.
"""

def square():
    squares_list = [num**2 for num in range(1,21)]
    print(squares_list[0:5])

square()

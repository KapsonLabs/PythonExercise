"""
Allan Katongole
13 December 2018
Checks whether 4 digit binary
numbers are divisible by 5
"""

def binary_diviser(num):
    items = []
    for b in num:
        x = int(b, 2)
        if not x%5:
            items.append(b)
    return ','.join(items)

if __name__ == '__main__':
    num = [x for x in input('Please input space seperated 4-digit binary numbers \n').split(',')]
    print(binary_diviser(num))

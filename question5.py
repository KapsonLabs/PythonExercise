"""
Allan Katongole
13 December 2018
Bank Account chap
"""

def bank_account():
    pass

if __name__ == '__main__':
    key, value = input().split(',')
    bank_dict = {}
    bank_dict[key] = value
    print(bank_account(bank_dict))
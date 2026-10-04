n = int(input("Enter a number: "))

def cal_odd_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(cal_odd_even(n))
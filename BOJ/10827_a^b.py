from decimal import Decimal
import sys
input = sys.stdin.readline

a, b = input().split()

a2 = int(float(a)*1000000000)
m = a2**int(b)

d = 1000000000**int(b)

quotient, remainder = divmod(m, d)
# int_part = int(m//d)
result = str(quotient)
if remainder:
    result += '.'
    # while m > 0:
    #     m -= x*d
    #     x = int(str(m)[0])
    #     result += str(x)
    result += str(m)[len(str(quotient)):].rstrip('0')

# result = Decimal(a)**Decimal(b)

print(result)

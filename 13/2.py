# Python 2.7
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
 
# if __name__ == '__main__':
#     n = [3, 5, 7]
#     a = [2, 3, 2]
#     print chinese_remainder(n, a)

with open('input.txt') as f:
  lines = f.read().splitlines()

buses = lines[1].split(",")

demands = []
divisors = []
rems = []
for bus in buses:
  if bus != 'x':
    n = int(bus)
    demands.append((n, (n - buses.index(bus)) % n))
    divisors.append(n)
    rems.append((n - buses.index(bus)) % n)
    
print(chinese_remainder(divisors, rems))
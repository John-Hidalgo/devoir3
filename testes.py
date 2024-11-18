import math
def D(n):
    if n == 1:
        return 7
    return 2 * D(n // 5) + n

def G(n):
    return int((16/3) * (n ** (math.log(2) / math.log(5))) + (5/3) * n)

n = 5
for i in range(1,10):
    n = 5**i
    print("valeur recursive =",D(n))
    print("valeur general =",G(n))
    assert D(n) == G(n)

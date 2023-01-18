import math

M = 20
N = 6

result = M / N

whole_divisor = math.floor(result)

mod = M - N*whole_divisor

print(mod)
print(M % N)


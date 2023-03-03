# 백준 14490_백대열

import math
import sys


n, m = map(int, sys.stdin.readline().split(":"))
gcd = math.gcd(n, m)
n //= gcd
m //= gcd

print("{}:{}".format(n, m))

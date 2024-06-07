# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p)
# How many different ways can £2 be made using any number of coins?
# 1, 2, 5, 10, 20, 50, 100, 200
# how many ways can those numbers add up to 200?
# 200 1s
# 100 2s
# 40 5s
# 20 10s
# 4 50s
# 2 100s
# 1 200
from datetime import datetime

print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
N = 200
K = [1, 2, 5, 10, 20, 50, 100, 200]
# 1 5, 2 2 & 1 1, 1 2 & 3 1, 5 1

dp = [0] * (N + 1)
dp[0] = 1

for row in K:
    for col in range(1, N + 1):
        if col >= row:
            dp[col] = dp[col] + dp[col - row]

print(dp[N])
print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

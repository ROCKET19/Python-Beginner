# https://codeforces.com/contest/617/problem/A  (Elephant)

origin = 0
x = int(input())
count = 0
for steps in range(origin, x, 5):
    count += 1
print(count)

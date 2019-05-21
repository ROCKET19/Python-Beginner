# https://codeforces.com/contest/705/problem/A (Hulk)

feeling = ''
n = int(input())
for count in range(1, n+1):
    if count % 2 == 0:
        feeling += 'that I love '
    elif count == 1:
        feeling += 'I hate '
    else:
        feeling += 'that I hate '
feeling += 'it'
print(feeling)
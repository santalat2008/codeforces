n = int(input())
s = list(map(int, input().split()))

t = sum(s)
if all(x <= 1 for x in s):
    print(0)
    exit()

h = 0
b = [i for i, x in enumerate(s) if x == 0]
k = [i for i, x in enumerate(s) if x > 1]

for i in k:
    while s[i] > 1:
        d = [(min(abs(i - x), n - abs(i - x)), x) for x in b]
        d.sort()
        dist, tg = d[0]
        s[i] -= 1
        s[tg] = 1
        h += dist
        b.remove(tg)

print(h)

zadachi = int(input())
n = 0
for _ in range(zadachi):
        opinions = list(map(int, input().split()))
        if sum(opinions) >= 2:
            n += 1
print(n)
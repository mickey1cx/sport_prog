# https://stepik.org/lesson/307318/step/2?unit=289406

n, m = map(int, input().split())
counters = []

for i in range(m):
    k = int(input())
    a = [1] * (n - k) + [0] * k

    l = -1
    r = n
    counter = 0
    while l + 1 < r:
        counter += 1
        mid = (l + r) // 2
        if a[mid] == 0:
            l = mid
        else:
            r = mid

    counters.append(counter)

print(*counters, sep='\n')

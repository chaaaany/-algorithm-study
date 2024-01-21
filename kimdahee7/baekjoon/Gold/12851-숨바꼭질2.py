from collections import deque

N, K = map(int, input().split())
INF = 1e9
time = [INF for _ in range(100010)]
answer = []

q = deque()
q.append(N)
time[N] = 0
# N == K일 경우도 고려
if N == K:
    answer.append(time[N])
while q:
    x = q.popleft()
    for i in x + 1, x - 1, 2 * x:
        if i < 0 or i >= 100010:
            continue

        # 가장 빠른 시간으로 도달하는 방법을 모두 찾아야 하므로 같을 경우도 고려
        if time[i] >= time[x] + 1:
            time[i] = time[x] + 1
            q.append(i)
            if i == K:
                answer.append(time[i])

print(time[K])
total = 0
for i in answer:
    if i == time[K]:
        total += 1
print(total)
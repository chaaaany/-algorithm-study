from collections import deque

N,M = map(int,input().split())
l = list(map(int,input().split()))
c = l.pop(0)
graph = [[] for _ in range(N+1)]
party = []
for _ in range(M):
  p = list(map(int,input().split()))
  p.pop(0)
  party.append(p)
  for i in p:
    for j in p:
      if j not in graph[i]:
        graph[i].append(j)

total = len(party)
visited = set()

q = deque(l)
while q:
  x = q.popleft()
  visited.add(x)
  for i in graph[x]:
    if i not in visited:
      visited.add(i)
      q.append(i)

for i in party:
  for j in visited:
    if j in i:
      total -=1
      break

print(total)
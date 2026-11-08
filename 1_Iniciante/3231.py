import sys
from collections import deque

def solve():

    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    N, H, L = map(int, input_data[0].split())
    
    horror_list = list(map(int, input_data[1].split()))
    
    graph = [[] for _ in range(N)]
    
    line_idx = 2
    for _ in range(L):
        if line_idx < len(input_data):
            u, v = map(int, input_data[line_idx].split())
            graph[u].append(v)
            graph[v].append(u)
            line_idx += 1

    hi = [-1] * N

    queue = deque()
    
    for movie in horror_list:
        hi[movie] = 0
        queue.append(movie)
        
    while queue:
        curr = queue.popleft()
        
        for neighbor in graph[curr]:

            if hi[neighbor] == -1:
                hi[neighbor] = hi[curr] + 1
                queue.append(neighbor)
                
    for i in range(N):
        if hi[i] == -1:
            hi[i] = float('inf')

    best_movie = -1
    max_hi = -1
    
    for i in range(N):
        if hi[i] > max_hi:
            max_hi = hi[i]
            best_movie = i
        elif hi[i] == max_hi:
            if i < best_movie:
                best_movie = i
                
    print(best_movie)

if __name__ == '__main__':
    solve()

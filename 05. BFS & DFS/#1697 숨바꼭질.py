# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:51:09 2021

@author: newave986.git
"""

#BOJ 1697

from collections import deque

def BFS(N, M, visited):

    count = 0
    
    queue = deque()
    queue.append([N, 0])

    while queue:
        k, count = queue.popleft()

        if k == M:
            break
        
        if visited[k] == False:
            
            count += 1
            visited[k] = True
            
            if (2*k < 100000):
                queue.append([2*k, count])
            
            if (0 < k+1 < 100000):
                queue.append([k+1, count])
                
            if (0 < k-1 < 100000):
                queue.append([k-1, count])
        
    print(count)

N, M = map(int, input().split())
visited = [False] * 100001
BFS(N, M, visited)

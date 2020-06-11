# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 00:19:20 2019

@author: hheim
"""



import heapq

def astar(grid, start, end):
    closed = {}
    openf = [(0, start)]
    openg = {start : 0}
    movements = [[0,1],[1,0],[0,-1],[-1,0]]
    
    #Main loop
    while openg:
        cost, current = heapq.heappop(openf)
        closed[current] = openg[current]
        del openg[current]
        if current == end:
            return cost
        for move in movements:
            child = tuple(map(add,current,move))
            if child not in closed and 0 <= child[0] <= len(grid[0])-1 and 0 <= child[1] <= len(grid)-1 and grid[child[0]][child[1]] != 1:
                g = closed[current]+1
                haux = tuple(map(sub,end,child))
                h = haux[0]**2+haux[1]**2
                f = g + h
            else:
                continue
            if child in openg:
                if openg[child] < g :
                    continue
            openg[child] = g
            heapq.heappush(openf, (f,child))
    
    return False
            
def path_finder3(string):
    grid = [[0 if elem == "." else 1 for elem in row] for row in string.split("\n")] 
    return astar(grid, (0,0), (len(grid[0])-1, len(grid)-1))    
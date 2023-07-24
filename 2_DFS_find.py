from queue import Queue

adj_list = {
    "A":["B","C"],
    "B":["D","E"],
    "C":["B", "F"],
    "D":[],
    "E":["F"],
    "F":[]
}

state = {}
trav_step = {}
parent = {}
dfs_traversal_op = []

target_node = "F"

for node in adj_list.keys():
    state[node] = "Idle"
    parent[node] = None
    trav_step[node] = [-1, -1]
    
step = 0

def dfs_func(u):
    global step
    state[u] = "Start"
    trav_step[u][0] = step
    dfs_traversal_op.append(u)
    step += 1
    
    if u == target_node:
        print(dfs_traversal_op)
    
    for v in adj_list[u]:
        if state[v] == "Idle":
            parent[v] = u
            if dfs_func(v):
                return True

    state[u] = "End"
    trav_step[u][1] = step
    step += 1
    return False
    
dfs_func("A")
# print(dfs_traversal_op)
from queue import Queue
adj_list = {
    "A" : ["B", "D"],
    "B" : ["A", "C"],
    "C" : [],
    "D" : ["E", "F"],
    "E" : ["F", "G"],
    "F" : ["E", "H"],
    "G" : ["E", "H"],
    "H" : ["G", "F"]
}
state = {} #Idle start end
parent = {}
trav_step = {} #[start, end]
dfs_traversal_op = []
for node in adj_list.keys():
    state[node] = "IDLE"
    parent[node] = None
    trav_step[node] = [-1, -1]
    
step = 0
def dfs_func(u):
    global step
    state[u] = "Start"
    trav_step[u][0] = step
    dfs_traversal_op.append(u)
    step += 1
    for v in adj_list[u]:
        if state[v] == "IDLE":
            parent[v] = u
            dfs_func(v)
            
    state[u] = "End"
    trav_step[u][1] = step
    step += 1

dfs_func("A")
print(dfs_traversal_op)
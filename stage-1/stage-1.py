import networkx as nx
import matplotlib.pyplot as plt
import random
import time
k = 8 # the degree of the network is 8
n = 10000 # the network has 10000 nodes
m = 10000 # the repeat iteration


test_set = [4490, 4500, 4510, 4520, 4530, 4540, 4550, 4560, 4570, 4580, 4590, 4600]
print_freq = 500

conn_prob = []
for i in test_set:
    num = 0
    com_n = 0
    time_start = time.time()
    for j in range(m):
        rg = nx.random_graphs.random_regular_graph(k, n)
        del_nodes = random.sample(range(0, n), i)
        for node in del_nodes:
            rg.remove_node(node)
        if nx.is_connected(rg) == True:
            if j % print_freq == 0:
                print('delete nodes: ', i, "iteration: ", j, 'connected')
            num += 1
        elif j % print_freq == 0:
            print('delete nodes: ', i, "iteration: ", j, 'disconnected')
    conn_prob.append(num / m)
    time_end = time.time()
    print('delete nodes: ', i, 'prob: ', num/m, 'time:', time_end - time_start)


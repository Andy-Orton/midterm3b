
# runs dijkstras algorithm for single source once for each given node then returns the minimum travel time
def two_friends_meet(graph, s, t):
    s_shortest = dijkstras(graph.copy(), s)
    t_shortest = dijkstras(graph.copy(), t)
    return(min(s_shortest[node] + t_shortest[node] for node in graph))



# takes in a graph that is represented by a dictionary of dictionary's
# graph = {'a': {'b': 3, 'd': 10}}
# a has two edges, one goes to b with weight 3, one goes to d with weight 10
# and a source node where we will find all the shortest paths from
def dijkstras(graph, source):
    shortest_distances = {}
    not_visited = graph

    # initialize shortest path for each node to be a really high number
    for node in not_visited:
        shortest_distances[node] = 99999999
    # sets shortest distance at source to 0
    shortest_distances[source] = 0

    while not_visited:
        minimum_node = None
        for node in not_visited:
            if minimum_node == None:
                minimum_node = node
            elif shortest_distances[node] < shortest_distances[minimum_node]:
                minimum_node = node
        
        for child, weight in graph[minimum_node].items():
            if weight + shortest_distances[minimum_node] < shortest_distances[child]:
                shortest_distances[child] = weight + shortest_distances[minimum_node]
        not_visited.pop(minimum_node)
    return shortest_distances




def test_two_friends():
    graph = {'a':{'b':7,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':10,'e':2},'d':{'e':9},'e':{'d':10}}
    assert two_friends_meet(graph, 'a', 'd') == 9

def test_two_friends2():
    graph = {'a':{'b': 3, 'c':1}, 'b':{'c':10}, 'c':{'a':1, 'b':10}}
    assert two_friends_meet(graph, 'a', 'b') == 3
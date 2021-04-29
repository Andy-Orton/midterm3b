
# 8.14

## Summary

The summary of this problem is that two friends live in different cities and want to minimize time to see eachother in person. These people are going to drive to a middle city.

## My solution

I think this problem is pretty simple. We can represent the cities and roads as a weighted graph with edges. It wouldn't make sense for the graph to have negative edges as you can't have negative travel time. We take in a graph, and a starting vertex for each of our friends. My solution would be to run Dijkstra's algorithm twice, one for one friends vertex, one for the other, then find the minimum sum for all vertexes in both given graphs. 

## Analysis of Correctness

We already know dijkstra's algorithm will give us the minimum cost it takes to get from a source node to each other node. The problem is asking for the minimum travel time from both starting nodes. All our algorithm is doing is finding the shortest path from both of our nodes to all other nodes, then finding the node which both vertexes travel time sums up to be the least.

## Analysis of Runtime

We know we run Dijkstra's algorithm twice, each time the algorithm is called the runtime is the same, O(ElogV) where E is the number of edges and V is the number of vertecies. The other part of the algorithm is finding the minimum sum. This loop loops through every node so the runtime is O(V). O(ElogV) dominates O(V) so the runtime is O(ElogV).


# 11.9

## Summary 

The problem consists of an n x n square grid where some grid pieces are white and some are black. 

* Every token needs to be on a white square
* Every row needs to contain exactly one token
* Every column needs exactly one token

The input consists of a two dimensional boolean array called IsWhite where every value is a boolean. True if the square is white, false if it isn't. The function should return true if it can find a place for all the pieces, false if it can't.

## My Solution

My solution involves the maxflow algorithm. We are going to create a start and an end node to absorb and create flow. 'n' row nodes to represent the rows. We connect the row nodes to the start node with a capacity of 1. We can then start accounting for the white squares. Whenever we find a white square we can add a node to the graph and connect it to the corresponding row node. These edges also have a capacity of 1. To account for the columns we also create n column nodes. The white square nodes have output to the corresponding column node. The edges that go into the column nodes from the white square nodes have a capacity of 1. Then we have the output of the column nodes go into the end node. We get the maxflow by summing the output of the column nodes. If the output is equal to n we know that we can fit n pieces onto the board without breaking any of the rules. 

## Analysis of Correctness

We know that we have to start somewhere so I started with the rows. I have n rows so I made n row nodes. These row nodes have an incoming edge from the start node that has a capacity of 1. These row nodes are connected to nodes representing all the white squares with an edge that has a capacity of 1. Because the edge has a capacity of 1 we know that the row node can only choose one white square to represent it, this property solves the second requirement. Because we only have nodes representing white squares the first requirement is automatically satisfied. We also have nodes that represent the columns. These nodes have a max output of one and have input from all of the white squares that are in the same column. This property satisfies the last requirement, proving that my maxflow solution is correct. 

## Runtime Analysis

We can assume that we are using Orlin's so the max flow algorithm takes O(VE). To convert the graph, we need to loop through the board and find all the white spaces, and add them to a list that corresponds to a row and a list that corresponds to a column. This will take O(n^2) to loop through the entire board. The O(n^2) dominates teh O(VE) so the runtime is O(n^2)


# 8.13

## Summary 

The problem is finding the number of shortest paths from s to t. Meaning that two paths from s to t with a weight of 4 would be considered 2 paths. 


## My Solution

The way my mind went with the hint was using Dijkstras algorithm to find the shortest paths from the starting vertex to every other vertex. We can find all the edges that are required. So now we have a graph of all the required edges. Then we need to count the number of ways to get to s to t in the subgraph. I would do this with a DFS from S to T counting all the unique ways to get to the T.

## Analysis of Correctness

Because we ran Dijkstras algorithm to find all the edges that are required, we know that all the edges given can give us the shortest paths from any vertex to any vertex. This by definition is the answer to the problem. 

## Runtime Analysis

We know that Dijkstras algorithm takes O(V log V). We also know that DFS takes linear time O(V + E). Dijkstras algorithm dominates the runtime so the final runtime of the algorithm is O(V log V).